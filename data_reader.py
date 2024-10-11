# модуль, отвечающий за чтение с порта

import serial
import serial.tools.list_ports

class DataReader:
    def __init__(self, port):
        self.port = port
        self.baudrate = 115200

    def check(self, port):
        available_ports = [port.device for port in serial.tools.list_ports.comports()]
        return port in available_ports

test = DataReader('COM4')
a = test.check('COM7')
print(a)

