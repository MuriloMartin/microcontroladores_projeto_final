import json
import numpy as np
import sounddevice as sd
from serial import Serial
import time as code_time

last_serial_write_time = 0
meu_serial = Serial(port='/dev/ttyUSB0', baudrate=9600)


# Load the vibration data (assuming you have already saved it as 'vibration_pattern.json')
with open('data/processed/nutcracker_vibration_pattern.json', 'r') as fp:
    vibration_data = json.load(fp)

low_energy = np.array(vibration_data['low'])
mid_energy = np.array(vibration_data['mid'])
high_energy = np.array(vibration_data['high'])
stft_times = np.array(vibration_data['stft_times'])
y = np.array(vibration_data['y'])
sr = np.array(vibration_data['sr'])



def callback(data, frames, time, status):
    current_time = time.outputBufferDacTime
    idx = np.argmin(np.abs(stft_times - current_time))

    low_intensity = low_energy[idx] 
    mid_intensity = mid_energy[idx]
    high_intensity = high_energy[idx]
    visualization = (
        f"L: {'#' * 2 * int(low_intensity)}".ljust(50) +  # Bass energy with fixed width
        f"M: {'*' * 2 * int(mid_intensity)}".ljust(50) +  # Mid energy with fixed width
        f"H: {'-' * 2 * int(high_intensity)}".ljust(50)  # Treble energy with fixed width
    )

    serial_string = "bass off\n"
    if low_intensity > int(1):
        serial_string = f"bass\n"

    global last_serial_write_time
    if code_time.time() - last_serial_write_time >= 0.1:
        print('------------------------ enviei info ------------------------')
        meu_serial.write(serial_string.encode("UTF-8"))
        last_serial_write_time = code_time.time()  
    
    
    print(visualization) 
    

    
with sd.InputStream(callback=callback, channels=1,samplerate=sr):
    sd.play(y, samplerate=sr)
    sd.wait() 

