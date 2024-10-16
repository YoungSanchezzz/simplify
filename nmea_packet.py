# модуль, описывающий пакет nmea
from tkinter.constants import PROJECTING


class Packet:
    def __init__(self, response, use_grabber):

        # значения пакета
        self.response = None # пришедший пакет
        self.pgn = None # pgn пакета
        self.value = None # значение пакета

        if use_grabber:
            self.response = str(response)
            self.pgn = self.response[17:21]
            self.value = self.response[24:47].split()
        else:
            self.response = response
            self.response[-1] = self.response[-1][:-2]
            pgn_unreverse = self.response[0]
            self.response.remove(self.response[0])
            self.value = self.response
            self.pgn =self.__reverse_pgn(pgn_unreverse)

    def __reverse_pgn(self, current):
        reverse = int(current) >> 8
        reverse = hex(reverse)
        reverse = reverse[-4:].upper()
        return reverse

