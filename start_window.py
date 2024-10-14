# стартовое окно программы

import customtkinter

class StartWindow(customtkinter.CTk):
    def __init__(self, port_callback):
        super().__init__()
        self.title('welcome page')
        self.geometry('400x200')
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')

        self.port_callback = port_callback

        # интерфейс окна
        self.enter_port = customtkinter.CTkEntry(self, placeholder_text='введите порт')
        self.enter_port.pack(pady = (40,20)) # поле ввода порта
        self.bind("<Map>", lambda event: self.set_focus())

        self.set_port = customtkinter.CTkButton(self, text='начать', command=self.__start_read)
        self.set_port.pack(pady=(0,20)) # кнопка "начать"
        self.bind('<Return>', lambda event: self.__start_read())

        self.condition = customtkinter.StringVar(value = "checked")
        self.use_grabber = customtkinter.CTkCheckBox(self, text='граббер')
        self.use_grabber.pack(pady = (0, 20)) # галочка "граббер"
        self.bind('<Tab>', lambda event: self.checkbox())

        self.bind('<Escape>', lambda event: self.destroy()) # кнопка esc


    def run(self):
        self.mainloop()

    def __start_read(self):
        port = str(self.enter_port.get())
        use_grabber = self.use_grabber.get()
        self.port_callback(port, use_grabber) # возвращаем порт в main в ф-цию get_port
        self.destroy()

    def set_focus(self):
        self.enter_port.focus()

    def checkbox(self):
        if self.use_grabber.get():
            self.use_grabber.deselect()
        else:
            self.use_grabber.select()
