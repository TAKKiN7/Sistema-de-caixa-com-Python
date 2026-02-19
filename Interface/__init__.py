from tkinter import *
from  tkinter import messagebox as msg
from Interface.Borda_Frame import Borda
from models.Caixa import Caixa
from database.database import Banco
from Interface.Saldo_Frame import Saldo_Frame
from Interface.Historico_Frame import Historico_Frame
from Interface.Janela_Acao import JanelaAcaoEntrada, JanelaAcaoSaida


class Janela(Tk):
    def __init__(self, caixa : Caixa, banco : Banco):
        super().__init__()
        self.caixa : Caixa = caixa
        self.banco : Banco = banco
        self.config_janela()
        self.bordas()
        self.layout()
        self.run()

    def config_janela(self):
        self.attributes("-fullscreen", True)
        self.protocol("WM_DELETE_WINDOW",lambda : ())
        self.configure(background="#1C2238")


    def layout(self):
        nomeL : Label = Label(self, text="CAIXA", font=("itim", 40, "bold"), bg="#171C2E", fg="WHITE")
        nomeL.place(relx=.1, rely=.0, relwidth=.8)

        self.frame_saldo()
        self.frame_historico()

        entradaB : Button = Button(self, text="Entrada", command=self.entrada, font=("itim", 20, "bold"), borderwidth=0, bg="#0f0",
                                   fg="WHITE")
        entradaB.place(relx=.26, rely=0.25, relwidth=.15)

        saidaB: Button = Button(self, text="Saída", command=self.saida, font=("itim", 20, "bold"), borderwidth=0, bg="#f00",
                                fg="WHITE")
        saidaB.place(relx=.42, rely=.25, relwidth=.16)

        relatorioB: Button = Button(self, text="Relatório", font=("itim", 20, "bold"), borderwidth=0, bg="#00f",
                                    fg="WHITE")
        relatorioB.place(relx=.59, rely=.25, relwidth=.15)

        self.fechar_button()


    def frame_historico(self):
        historico_frame : Frame = Historico_Frame(self)

    def frame_saldo(self):
        self.saldo: StringVar = StringVar()
        self.saldo.set(self.saldo_formatado())
        self.saldoF: Frame = Saldo_Frame(self, self.saldo)

    def fechar_button(self):
        sairB: Button = Button(self, text="Sair", font=("itim", 10, "bold"),
                               bg="#9b111e", fg="WHITE", command=self.fechar, borderwidth=0)
        sairB.place(relx=.8, rely=.01, relwidth=.08)


    def bordas(self):
        bordaL : Borda = Borda(self)
        bordaL.place(relx=0, rely=0, relwidth=.1, relheight=1)

        bordaR : Borda = Borda(self)
        bordaR.place(relx=.9, rely=0, relwidth=.1, relheight=1)


    def saldo_formatado(self) -> str:
        saldo : float = self.caixa.saldo
        saldot : str = str(f"{saldo:.2f}").replace(".", ",")

        return saldot

    def run(self):
        self.mainloop()


    def fechar(self):
        res = msg.askokcancel("Fechar", "Tem certeza que deseja fechar?")
        if not res:
            return
        self.destroy()



    def atualizar_saldo(self):
        self.saldo.set(self.saldo_formatado())

    def entrada(self):
        janela : JanelaAcaoEntrada = JanelaAcaoEntrada(self, self.caixa, self.banco, self.atualizar_saldo)
        #self.caixa.entrada(100)
        #self.banco.atualizar_caixa(self.caixa)
        self.saldo.set(self.saldo_formatado())


    def saida(self):
        janela : JanelaAcaoSaida = JanelaAcaoSaida(self, self.caixa, self.banco, self.atualizar_saldo)
        #self.caixa.saida(100)
        #self.banco.atualizar_caixa(self.caixa)
        #self.saldo.set(self.saldo_formatado())