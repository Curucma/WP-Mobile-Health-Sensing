"""
code from: https://core-electronics.com.au/guides/piicodev-three-axis-accelerometer-lis3dh-getting-started-guide/#A4I60M9
PiicoDev Accelerometer LIS3DH
Simple example to read acceleration data
"""

from PiicoDev_LIS3DH import PiicoDev_LIS3DH
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function
from time import sleep

motion = PiicoDev_LIS3DH(bus = 0, sda =4, scl=5, rate = 25) # Initialise the accelerometer

motion.range = 2 # Set the range to +-2g

while True:
    x, y, z = motion.acceleration
    x = round(x,2) # round data for a nicer-looking print()
    y = round(y,2)
    z = round(z,2)
    myString = "X: " + str(x) + ", Y: " + str(y) + ", Z: " + str(z) # build a string of data
    print(myString)

    sleep_ms(5)