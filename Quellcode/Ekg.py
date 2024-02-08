# Bibliotheken laden
from machine import ADC
from time import sleep

# Initialisierung des ADC2
sensor = ADC(2)


# Wiederholung einleiten (Schleife)
while True:
    # Temparatur-Sensor als Dezimalzahl lesen
    value_a = sensor.read_u16()
   
    # Ausgabe in der Kommandozeile/Shell
    print(value_a)
  
    # 2 Sekunden warten
    sleep(0.01)
