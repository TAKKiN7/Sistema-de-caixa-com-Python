from tkinter import *
from  tkinter import messagebox as msg
from Interface.Borda_Frame import Borda
from models.Caixa import Caixa
from database.database import Banco

class Janela(Tk):
    def __init__(self, caixa : Caixa):
        super().__init__()
        self.caixa : Caixa = caixa
        self.config_janela()
        self.bordas()
        self.layout()
        self.run()

    def config_janela(self):
        self.attributes("-fullscreen", True)
        #self.protocol("WM_DELETE_WINDOW", self.fechar)


    def layout(self):
        nomeL : Label = Label(self, text="CAIXA", font=("itim", 40, "bold"))
        nomeL.place(relx=.45, rely=.01, relwidth=.20)


        self.saldo : StringVar = StringVar()
        self.saldo.set("10,00")

        saldoL : Label = Label(self, text="Saldo R$:", font=("itim", 20, "bold"))
        saldoL.place(relx=.6, rely=.15)

        caixaL : Label = Label(self, textvariable=self.saldo, font=("itim", 30, "bold"))
        caixaL.place(relx=.7, rely=.14)

        entradaB : Button = Button(self, text="Entrada")
        entradaB.place(relx=.15, rely=0.35)

        saidaB: Button = Button(self, text="Saída", command=self.teste)
        saidaB.place(relx=.15, rely=0.4)


    def bordas(self):
        bordaL : Borda = Borda(self)
        bordaL.place(relx=0, rely=0, relwidth=.2, relheight=1)

        bordaR : Borda = Borda(self)
        bordaR.place(relx=.9, rely=0, relwidth=.1, relheight=1)


    def teste(self):
        saldo : float = self.caixa.saldo
        saldot : str = str(f"{saldo:.2f}").replace(".", ",")
        self.saldo.set(saldot)

    def run(self):
        self.mainloop()


    def fechar(self):
        res = msg.askokcancel("Fechar", "Tem certeza que deseja fechar?")
        if not res:
            return
        self.destroy()
