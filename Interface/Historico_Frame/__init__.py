from tkinter import Frame


class Historico_Frame(Frame):
    def __init__(self, root):
        super().__init__(root, highlightthickness=2, bg="#222A45", highlightbackground="BLACK")
        self.layout()


    def layout(self):
        self.place(relx=.25, rely=0.6, relwidth=.47, relheight=.25)
