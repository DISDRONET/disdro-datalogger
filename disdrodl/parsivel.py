import serial
from .disdrometer import Disdrometer

BAUD = 19200
READ_DELAY = 1


class Parsivel(Disdrometer):
    def __init__(self, device='/dev/ttyUSB0'):
        super().__init__()
        self.ser = serial.Serial(device, BAUD, timeout=READ_DELAY)

    def readline(self):
        self.ser.readline()
