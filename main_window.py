# основное окно, отображающее данные
import threading

import customtkinter


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('blue boat')
        self.geometry('400x600')


        #интерфейс программы
        self.coords = customtkinter.CTkLabel(self, text = 'координаты судна: ')
        self.coords.grid(row = 0, column = 0, padx = 10 ,pady = 20, sticky='nsw') # координаты судна
        self.coords_value = customtkinter.CTkLabel(self, text='широта | долгота')
        self.coords_value.grid(row=0, column=1, padx=10, pady=20, sticky='nsw')

        self.speed = customtkinter.CTkLabel(self, text = 'скорость судна: ')
        self.speed.grid(row = 1, column = 0, padx = 10, pady = 20, sticky='nsw') # скорость судна
        self.speed_value = customtkinter.CTkLabel(self, text= '0 м/c')
        self.speed_value.grid(row = 1, column = 1, padx = 10, pady = 20, sticky='nsw')

        self.bind('<Escape>', lambda event: self.destroy())


    def run(self):
        self.mainloop()

    def update(self, decoded_data):
        match decoded_data.pgn:
            case 'F801':
                self.coords_value.configure(text=f'{decoded_data.latitude} | {decoded_data.longitude}')
            case 'F802':
                self.speed_value.configure(text=f'{decoded_data.sog} м/c')
