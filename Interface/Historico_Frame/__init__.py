from customtkinter import CTkFrame


class Historico_Frame(CTkFrame):
    def __init__(self, root):
        super().__init__(root, border_width=2, bg_color="#1C2238", fg_color="#222A45", border_color="BLACK", corner_radius=20)
        self.layout()


    def layout(self):
        self.place(relx=.25, rely=0.6, relwidth=.5, relheight=.25)
