from customtkinter import CTkFrame, CTkLabel, StringVar


class Saldo_Frame(CTkFrame):
    def __init__(self, root, saldo : StringVar):
        super().__init__(root, border_width=2, bg_color="#1C2238", fg_color="#222A45", border_color="BLACK", corner_radius=20)
        self.saldo : StringVar = saldo
        self.layout()



    def layout(self):
        saldoL : CTkLabel = CTkLabel(self, text="Saldo Atual", font=("itim", 13, "bold"), text_color="white", fg_color="#222A45")
        saldoL.place(relx=.425, rely=.08, relwidth=.15)


        self.caixaL : CTkLabel = CTkLabel(self, textvariable=self.saldo, font=("itim", 50, "bold"), text_color="WHITE", fg_color="#222A45")
        self.caixaL.place(relx=.35 , rely=.3, relwidth=.3)

        self.place(relx=.25, rely=0.34 ,relwidth=.5, relheight=.25)
