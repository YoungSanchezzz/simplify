# точка входа в программу

from start_window import StartWindow

class Main:
    def __init__(self):

        self.start_window = StartWindow() # объект стартового окна
        self.start_window.run()



app = Main()


