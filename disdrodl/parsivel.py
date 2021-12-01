from .disdrometer import Disdrometer
import time


class Parsivel(Disdrometer):
    def __init__(self):
        super().__init__()

    def configure(self):
        self.set_real_time()

    # TODO: ask Rob details
    def ask_real_time(self, command='CS/U\r'):
        self.ser.write(command.encode('utf-8'))

    def set_real_time(self, command=f'CS/U/{time.strftime("%d.%m.%Y %H:%M:%S")}\r'):
        self.ser.write(command.encode('utf-8'))

    def restart(self, command='CS/Z/1\r'):
        self.ser.write(command.encode('utf-8'))

    def ask_user_telegram(self, command='CS/M/M/1\r'):
        self.ser.write(command.encode('utf-8'))
