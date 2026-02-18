from tkinter import Frame, Label, StringVar


class Saldo_Frame(Frame):
    def __init__(self, root, saldo : StringVar):
        super().__init__(root, highlightthickness=2, bg="#222A45", highlightbackground="BLACK")
        self.saldo : StringVar = saldo
        self.layout()



    def layout(self):
        saldoL : Label = Label(self, text="Saldo Atual", font=("itim", 13, "bold"), fg="white", bg="#222A45")
        saldoL.place(relx=.425, rely=.08, relwidth=.15)


        self.caixaL : Label = Label(self, textvariable=self.saldo, font=("itim", 50, "bold"), fg="GREEN", bg="#222A45")
        self.caixaL.place(relx=.35 , rely=.3, relwidth=.3)

        self.place(relx=.25, rely=0.34 ,relwidth=.47, relheight=.25)
