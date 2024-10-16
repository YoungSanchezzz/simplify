# точка входа в программу
import threading


from start_window import StartWindow
from data_reader import DataReader
from main_window import MainWindow
from nmea_packet import Packet
from decoder_grabber import DecoderGrabber

class Main:
    def __init__(self):

        self.port = None # используемый порт
        self.response = None # приходящий пакет данных
        self.use_grabber = None # используем ли мы граббер
        self.packet = None # пакет nmea
        self.decoded_data = None # расшифрованные данные


        self.start_window = StartWindow(self.get_port) # объект стартового окна
        self.start_window.run()

        if self.port:
            self.main_window = MainWindow() # объект главного окна в приложении


    def get_port(self, port, use_grabber): # необходимо для получения порта из стартовой страницы
        self.port = port
        self.use_grabber = use_grabber

    def update(self):
        self.reader = DataReader(self.port)  # объект считывателя данных
        self.reader.start_reading()
        while True:
            self.response = self.reader.get_data()

            if not self.use_grabber:
                self.response = str(self.response).split(',')

                if len(self.response[0]) != 9:
                    continue
                self.packet = Packet(self.response, self.use_grabber)
                self.decoded_data = DecoderGrabber(self.packet, self.use_grabber)  # здесь лежит значение, которое надо отобразить
            else:
                self.packet = Packet(self.response, self.use_grabber)  # здесь у нас лежит pgn и value
                # проверка, откуда получаем данные (из граббера или с платы)
                self.decoded_data = DecoderGrabber(self.packet)  # здесь лежит значение, которое надо отобразить
                # print('PGN:', self.packet.pgn, 'значение:', self.packet.value, 'сырье:', self.response)
            self.main_window.update(self.decoded_data)

    def run(self):
        threading.Thread(target=self.update, daemon=True).start() # поток обновлений
        self.main_window.run()


app = Main()
app.run()
