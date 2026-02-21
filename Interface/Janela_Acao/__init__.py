from customtkinter import CTkToplevel, CTkButton, CTkLabel, CTkEntry, StringVar
from tkinter import messagebox as msg
from database.database import Banco
from models.Caixa import Caixa

class JanelaAcao(CTkToplevel):
    def __init__(self, root, acao : str, caixa : Caixa, banco : Banco):
        super().__init__(root)
        self.caixa = caixa
        self.banco = banco
        self.acao : str = acao
        self.titulo : str = acao.upper()
        self.config()
        self.layout()

    @property
    def acao(self):
        return self._acao

    @acao.setter
    def acao(self, acao):
        if acao.lower() == "entrada":
            self._acao = "GREEN"
        else:
            self._acao = "RED"

    def config(self):
        self.grab_set()
        larguraT = self.winfo_screenwidth()
        alturaT = self.winfo_screenheight()
        self.overrideredirect(True)
        self.geometry(f"350x200+{int((larguraT / 2) - (350 / 2))}+{int((alturaT / 2) - 200 / 2)}")
        self.configure(fg_color=self.acao)



    def layout(self):
        tituloL : CTkLabel = CTkLabel(self, text=self.titulo, fg_color="BLACK", text_color="WHITE", font=("Arial", 20, "bold"))
        tituloL.place(relx=.0, rely=.0, relwidth=1)

        self.valorE : CTkEntry = CTkEntry(self, textvariable=StringVar(), font=("itim", 15, "bold"))
        self.valorE.bind("<Return>", lambda e: self.confirmar(e))
        self.valorE.place(relx=.35, rely=.3, relwidth=.3)
        self.valorE.focus_set()

        confirmarB : CTkButton = CTkButton(self, text="Confirmar", command =self.confirmar, border_width=1,
                                     border_color="WHITE")
        confirmarB.place(relx=.6, rely=.8, relwidth=.3)

        cancelarB : CTkButton = CTkButton(self, text="Cancelar",command=self.cancelar)
        cancelarB.place(relx=.1, rely=.8, relwidth=.3)


    def cancelar(self):
        self.destroy()

    def confirmar(self, e = None):
        pass




class JanelaAcaoEntrada(JanelaAcao):
    def __init__(self, root, caixa, banco, fun, acao : str = "entrada"):
        super().__init__(root, acao, caixa, banco)
        self.fun = fun

    def confirmar(self, e = None):
        try:
            valor = float(self.valorE.get().replace(",", "."))
            res: str = f"{valor:.2f}".replace(".", ",")
        except ValueError:
            msg.showerror("Erro", "Valor inválido")
        else:
            msg.showinfo("Finalizado", f"Registro de entrada realizado: R${res}")
            self.atualizar_saldo(valor)
            self.fun()
            self.destroy()


    def atualizar_saldo(self, valor):
        self.caixa.entrada(valor)
        self.banco.atualizar_caixa(self.caixa)



class JanelaAcaoSaida(JanelaAcao):
    def __init__(self, root, caixa, banco, fun, acao: str = "saida"):
        super().__init__(root, acao, caixa, banco)
        self.fun = fun

    def confirmar(self, e = None):
        try:
            valor : float = float(self.valorE.get().replace(",","."))
            res : str = f"{valor:.2f}".replace(".", ",")
        except ValueError:
            msg.showerror("Erro", "Valor inválido")
        else:
            msg.showinfo("Finalizado", f"Registro de saída realizado: R${res}")
            self.atualizar_saldo(valor)
            self.fun()
            self.destroy()

    def atualizar_saldo(self, valor):
        self.caixa.saida(valor)
        self.banco.atualizar_caixa(self.caixa)
