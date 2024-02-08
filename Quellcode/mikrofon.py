from machine import ADC
from time import sleep

import utime
 
analog_value = machine.ADC(2)

conversion_factor =3.3/(65536)

while True:
    reading = analog_value.read_u16()*conversion_factor
    print(reading)
    sleep(0.01) 
