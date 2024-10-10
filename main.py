# точка входа программы
from main_window import MainWindow
from start_window import StartWindow
from data_reader import DataReader

class Main:
    def __init__(self):

        self.port = None # порт программы

        # вызов окна для ввода порта
        self.start_window = StartWindow(self.port_check)
        self.start_window.run()

        # вызов основного окна
        self.main_window = MainWindow()

    def port_check(self, port): # функция получения порта
        self.port = port
        callback = DataReader(port).check()
        if callback:
            self.start_window.destroy()
        else:
            pass




app = Main()
