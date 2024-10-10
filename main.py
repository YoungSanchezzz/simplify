# точка входа программы
from main_window import MainWindow
from start_window import StartWindow
from data_reader import DataReader

class Main:
    def __init__(self):

        self.port = None # порт программы
        self.use_grab = None # если считываем с граббера

        # вызов окна для ввода порта
        self.start_window = StartWindow(self.port_check)
        self.start_window.run()

        self.main_window.print()



    def port_check(self, port, grab): # функция получения порта
        self.port = port
        self.use_grab = grab
        print(self.use_grab)
        callback = DataReader(port).check()
        if callback:
            self.start_window.destroy()
            # вызов основного окна
            self.main_window = MainWindow()
            self.main_window.run()
        else:
            pass




app = Main()
