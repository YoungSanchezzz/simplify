# стартовое окно программы

import customtkinter

class StartWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('welcome page')
        self.geometry('400x200')
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')

        # интерфейс окна
        self.enter_port = customtkinter.CTkEntry(self, placeholder_text='введите порт')
        self.enter_port.pack(pady = (40,20)) # поле ввода порта

        self.set_port = customtkinter.CTkButton(self, text='начать', command=self.__start_read)
        self.set_port.pack(pady=(0,20)) # кнопка "начать"

    def run(self):
        self.mainloop()

    def __start_read(self):
        port = str(self.enter_port.get())


    def end(self):
        self.destroy()