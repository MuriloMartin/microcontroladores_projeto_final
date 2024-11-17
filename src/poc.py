import librosa
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sounddevice as sd

filename = librosa.example('nutcracker')
y, sr = librosa.load(filename, sr=None)

hop_length = 512
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length)
beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=hop_length)

D = librosa.stft(y, hop_length=hop_length)
frequencies = librosa.fft_frequencies(sr=sr)
magnitude, _ = librosa.magphase(D)
bass_band = np.where((frequencies >= 20) & (frequencies < 320))[0]
bass_energy = np.mean(magnitude[bass_band, :], axis=0)
stft_times = librosa.frames_to_time(np.arange(bass_energy.shape[0]), sr=sr, hop_length=hop_length)


def callback(data, frames, time, status):
    current_time = time.outputBufferDacTime
    idx = np.argmin(np.abs(stft_times - current_time))
    intensity = bass_energy[idx]
    num_hashes = int(intensity * 3)  
    print('#' * num_hashes)  

    
with sd.InputStream(callback=callback, channels=1,samplerate=sr):
    sd.play(y, samplerate=sr)
    sd.wait() 