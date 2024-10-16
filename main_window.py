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
        self.coords.grid(row = 0, column = 0, padx = 10 ,pady = (20, 0), sticky='nsw') # координаты судна
        self.coords_value = customtkinter.CTkLabel(self, text='широта | долгота')
        self.coords_value.grid(row=0, column=1, padx=10, pady=(20, 0), sticky='nsw')

        self.speed = customtkinter.CTkLabel(self, text = 'скорость судна: ')
        self.speed.grid(row = 1, column = 0, padx = 10, pady = (10, 0), sticky='nsw') # скорость судна
        self.speed_value = customtkinter.CTkLabel(self, text= '0 м/c')
        self.speed_value.grid(row = 1, column = 1, padx = 10, pady = (10, 0), sticky='nsw')

        self.cog = customtkinter.CTkLabel(self, text='истинный курс судна: ')
        self.cog.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='nsw')  # истинный курс судна
        self.cog_value = customtkinter.CTkLabel(self, text='0 градусов')
        self.cog_value.grid(row=2, column=1, padx=10, pady=(10, 0), sticky='nsw')

        self.water_t = customtkinter.CTkLabel(self, text='температура воды: ')
        self.water_t.grid(row=3, column=0, padx=10, pady=(10, 0), sticky='nsw')  # температура воды
        self.water_t_value = customtkinter.CTkLabel(self, text='0 градусов')
        self.water_t_value.grid(row=3, column=1, padx=10, pady=(10, 0), sticky='nsw')




        self.bind('<Escape>', lambda event: self.destroy())


    def run(self):
        self.mainloop()

    def update(self, decoded_data):
        match decoded_data.pgn:
            case 'F801':
                self.coords_value.configure(text=f'{decoded_data.latitude} | {decoded_data.longitude}')
            case 'F802':
                self.speed_value.configure(text=f'{decoded_data.sog} м/c')
                self.cog_value.configure(text=f'{decoded_data.cog} градусов')
            case 'FD06': self.water_t_value.configure(text=f'{decoded_data.water_t} градусов')
