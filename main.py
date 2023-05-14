# VPPI main file

import serial
from serial.tools import list_ports


# Builtin Names
class Digital:  pass
class Analogue: pass

class High:
    def __init__(self):
        self.bool = True
        self.int = 1
    def __repr__(self):
        return "DigitalHigh"
class Low:
    def __init__(self):
        self.bool = False
        self.int = 0
    def __repr__(self):
        return "DigitalLow"

# Classes
class Pin:
    def __init__(self, type):
        self.dataType = type
        if type == Digital:
            self.value = Low
        elif type == Analogue:
            self.value = 0
        else:
            self.value = None


pins = [ Pin(Digital), Pin(Digital), Pin(Digital) ]


def main():
    for i in serial.tools.list_ports.comports():
        print(i)

    ser = serial.Serial(input("PORT: "), 115200)

    while True:
        ser.write(bytearray(input("Message: ") + "\n", "ascii"))


if __name__ == "__main__":
    main()
