# модуль, отвечающий за чтение с порта
import threading
import time

import serial
import serial.tools.list_ports

class DataReader:
    def __init__(self, port):
        self.port = port
        self.baudrate = 115200
        self.response = None

    def start_reading(self):
        """Запускает поток для чтения данных с порта."""
        self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        threading.Thread(target=self.read_data, daemon=True).start()

    def read_data(self):
        """Читает данные с порта в отдельном потоке."""
        while True:
            self.response = self.ser.readline().decode('utf-8')  # Чтение строки
            time.sleep(0.1)  # Задержка для уменьшения использования CPU

    def get_data(self):
        """Возвращает последние считанные данные."""
        return self.response



