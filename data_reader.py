# модуль чтения данных с порта

import serial
import threading
import time

class DataReader:
    def __init__(self, port):
        self.port = port # порт, введённый пользователем
        self.baudrate = 115200

    def check(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            print('порт открыт')
            return 1
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return 0
