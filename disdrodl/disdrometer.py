from .utils import get_device_type
from dataclasses import dataclass
import serial
import logging

PARSIVEL_BAUD = 19200
THIES_BAUD = 9600
READ_DELAY = 1

logger = logging.getLogger('disdrometer_logger')
logger.setLevel(logging.INFO)


@dataclass
class Disdrometer:
    """Class representing a disdrometer.

    Attributes
        device_type (str): The device type.
        device_port (str): The device port.
    """
    device_type: str = 'parsivel'
    device_port: str = '/dev/ttyUSB0'
    ser: serial.Serial = serial.Serial(timeout=READ_DELAY)

    def connect(self):
        """
        Method to connect to the device through serial.
        """
        self.ser.port = self.device_port
        if self.device_type == 'parsivel':
            self.ser.baudrate = PARSIVEL_BAUD
        elif self.device_type == 'thies':
            self.ser.baudrate = THIES_BAUD

        try:
            self.ser.open()
            logger.info("Device connected!")
        except Exception as e:
            logger.error('Failed to connect: ' + str(e))

        self.ser.reset_input_buffer()
