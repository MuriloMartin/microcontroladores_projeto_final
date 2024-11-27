from serial import Serial
from time import sleep


meu_serial = Serial(port='/dev/ttyUSB0', baudrate=9600)

lista = [["bass 30",0.5],["bass 60",0.5],["bass 100",0.5],["bass 150",0.5],["bass 200",0.5],["bass 255",0.5]]


sleep(2)

for i in lista:
    meu_serial.write((i[0]+"\n").encode("UTF-8"))
    print(i[0])
    print(i[1])
    sleep(i[1])