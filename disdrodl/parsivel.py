import serial
import time
# import sys

BAUD=19200

#TODO ask Rob if this is the right timeout
READ_DELAY=1

#TODO maybe create a class "Disdrometer" that contains all the functions
# common to all the parsivels and thies devices

# define a Parsivel class
class Parsivel(object):
    """
    Initialize the device
    :param device: /dev/yourConsoleDevice (e.g. /dev/ttyUSB0)
    """
    def __init__(self, device):
        self.ser = serial.Serial(device, BAUD, timeout=READ_DELAY)
    
    # define a function to connect to the serial port
    def readline(self):
        self.ser.readline()
        