from .disdrometer import Disdrometer


class Parsivel(Disdrometer):
    def __init__(self):
        super().__init__()

    def configure(self):
        self.ser.readline()
