from serial import Serial
from time import sleep


meu_serial = Serial(port='COM5', baudrate=9600)

lista = [["bass",0.1],["bass",0.5],["bass",0.5],["bass",0.1],["bass",0.5],["bass",0.8],["bass",1]]

sleep(2)

for i in lista:
    meu_serial.write((i[0]+"\n").encode("UTF-8"))
    print(i[0])
    print(i[1])
    sleep(i[1])