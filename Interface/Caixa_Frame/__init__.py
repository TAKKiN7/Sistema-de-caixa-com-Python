from tkinter import Frame


class Caixa(Frame):
    def __init__(self, root):
        super().__init__(root, background="RED")
        self.layout()

    
    def layout(self):
        self.place(relx=0, rely=0, relwidth=1, relheight=1)