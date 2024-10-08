# стартовое окно, запрашивающее порт
from urllib.parse import uses_query

import customtkinter
import threading

class StartWindow(customtkinter.CTk):
    def __init__(self, port_callback):
        super().__init__()
        self.title('enter port page')
        self.geometry('400x200')
        self.port_callback = port_callback

        # интерфейс окна
        self.set_port = customtkinter.CTkEntry(self, placeholder_text='введите порт')
        self.set_port.pack(pady=(40,0)) # поле для ввода порта

        self.start_button = customtkinter.CTkButton(self, text='начать', command=self.__start)
        self.start_button.pack(pady = 10) # кнопка старта

        self.use_grabber = customtkinter.CTkCheckBox(self, text='граббер')
        self.use_grabber.pack(pady=(0,10))

    def run(self):
        self.mainloop()

    def __start(self): # действия, которые выполняет кнопка старт
        port = str(self.set_port.get())
        grab = None
        if self.use_grabber.get():
            grab = 1
        else:
            grab = 0
        self.port_callback(port, grab)


