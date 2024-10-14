# модуль, описывающий пакет nmea

class Packet:
    def __init__(self, response, use_grabber):

        # значения пакета
        self.response = str(response) # пришедший пакет
        self.pgn = None # pgn пакета
        self.value = None # значение пакета

        if use_grabber:
            self.pgn = self.response[17:21]
            self.value = self.response[24:47].split()
        else:
            self.response =self.response.split(',')
            pgn_unreverse = self.response[0]
            self.value = self.response.remove(self.response[0])
            self.pgn =self.__reverse_pgn(pgn_unreverse)

    def __reverse_pgn(self, current):
        reverse = int(current) >> 8
        reverse = hex(reverse)
        reverse = reverse[-4:]
        return reverse

