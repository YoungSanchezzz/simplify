import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('blue boat')
        self.geometry('400x600')



app = App()
app.mainloop()

