# модуль декодера для граббера
import math


class DecoderGrabber:
    def __init__(self, packet, use_grabber):

        self.packet = packet # пришедший пакет
        self.pgn = self.packet.pgn
        self.use_grabber = use_grabber

        # передающиеся данные
        '''
        пакет F801 передает:
        latitude - координаты широты
        longitude - координаты долготы
        '''
        self.latitude, self.longitude = None, None

        '''
        пакет F802 передает:
        sid - ???
        cog - истинный курс судна
        sog - скорость судна
        '''
        self.sid, self.cog, self.sog = None, None, None


        match self.pgn:
            case 'F801': self.latitude, self.longitude = self.f801(self.packet.value)
            case 'F802': self.sid, self.cog, self.sog = self.f802(self.packet.value)



    def f801(self, input_value):
        # разбиваем на первые 4 значения и на вторые 4 значения
        group1, group2 = input_value[0:4], input_value[4:]
        lat = float(str(self.__converter(group1) * 10 ** -7)[:10])
        long = float(str(self.__converter(group2) * 10 ** -7)[:10])
        return lat, long

    def f802(self, input_value): #sid, cog, sog
        group1, group2, group3 = input_value[0], input_value[2:4], input_value[4:6]
        sid, cog, sog = int(self.__converter(group1)), self.__converter(group2), self.__converter(group3)
        cog = float(str(cog * 10 ** -4 * (180/math.pi))[:6])
        sog= float(str(sog * 10 ** -2 *3.6)[:6])
        return sid, cog, sog


    def __converter(self, group): # конвертация в hex
        if not self.use_grabber:
            group = [format(int(value), 'X') for value in group]
            for i in range(len(group)):
                if len(group[i]) == 1:
                    group[i] = '0' + group[i]
        reverse_str = group[::-1]  # little endian
        combined_str = ''.join(reverse_str)  # Собираем все значения массива в одну строку
        decimal_value = int(combined_str, 16)  # Переводим из HEX в decimal
        return decimal_value
