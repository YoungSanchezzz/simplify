# основное окно программы

import customtkinter

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('blue boat')
        self.geometry('400x600')
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')