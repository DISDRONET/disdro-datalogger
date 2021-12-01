from dataclasses import dataclass


@dataclass
class Disdrometer:
    """This is a class representing a disdrometer.

    Attributes
        device_type (str): The device type.
    """
    device_type: str

    def configure(self):
        if self.device_type == 'parsivel':
            pass
        elif self.device_type == 'this':
            pass
