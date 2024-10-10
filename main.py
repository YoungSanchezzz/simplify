# точка входа программы

from start_window import StartWindow

class Main:
    def __init__(self):

        self.port = None # порт программы

        # вызов окна для ввода порта
        self.start_window = StartWindow(self.entered_port)
        self.start_window.run()
        print(self.port)



    def entered_port(self, port): # функция получения порта
        self.port = port



app = Main()
