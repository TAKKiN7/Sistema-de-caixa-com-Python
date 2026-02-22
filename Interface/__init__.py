from customtkinter import *
from  tkinter import messagebox as msg
from Interface.Borda_Frame import Borda
from models.Caixa import Caixa
from database.database import Banco
from Interface.Saldo_Frame import Saldo_Frame
from Interface.Historico_Frame import Historico
from Interface.Janela_Acao import JanelaAcaoEntrada, JanelaAcaoSaida


class Janela(CTk):
    def __init__(self, caixa : Caixa, banco : Banco):
        super().__init__()
        self.caixa : Caixa = caixa
        self.banco : Banco = banco
        self.config_janela()
        #self.bordas()
        self.layout()
        self.run()

    def config_janela(self):
        self.attributes("-fullscreen", True)
        self.protocol("WM_DELETE_WINDOW",lambda : ())
        self.configure(fg_color="#1C2238")


    def layout(self):
        nomeL : CTkLabel = CTkLabel(self, text="CAIXA", font=("itim", 40, "bold"), fg_color="#171C2E", text_color="WHITE")
        nomeL.place(relx=0, rely=.0, relwidth=1)

        self.frame_saldo()

        entradaB : CTkButton = CTkButton(self, text="Entrada", command=self.entrada, font=("itim", 20, "bold"), border_width=0, fg_color="#00ff00",
                                   text_color="WHITE", hover_color="#0ab90a")
        entradaB.place(relx=.26, rely=0.25, relwidth=.15, relheight=.06)

        saidaB: CTkButton = CTkButton(self, text="Saída", command=self.saida, font=("itim", 20, "bold"), border_width=0, fg_color="#ff0000",
                                text_color="WHITE", hover_color="#c70606")
        saidaB.place(relx=.42, rely=.25, relwidth=.16, relheight=.06)

        relatorioB: CTkButton = CTkButton(self, text="Relatório", font=("itim", 20, "bold"), border_width=0, fg_color="#0000ff",
                                    text_color="WHITE", hover_color="#0000c7",
                                    command=self.historico)
        relatorioB.place(relx=.59, rely=.25, relwidth=.15, relheight=.06)

        self.fechar_button()

    def frame_saldo(self):
        self.saldo: StringVar = StringVar()
        self.saldo.set(self.saldo_formatado())
        self.saldoF: CTkFrame = Saldo_Frame(self, self.saldo)


    def fechar_button(self):
        sairB: CTkButton = CTkButton(self, text="Sair", font=("itim", 13, "bold"),
                               fg_color="#9b121f", hover_color="#5c0a12", text_color="WHITE",
                               command=self.fechar, border_width=0)
        sairB.place(relx=.9, rely=.01, relwidth=.08)


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

    def historico(self):
        self.janela_historico : Historico = Historico(self)
       
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