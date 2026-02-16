from tkinter import *
from  tkinter import messagebox as msg
from Caixa_Frame import Caixa

class Janela(Tk):
    def __init__(self):
        super().__init__()
        self.config_janela()
        self.layout()
        self.run()

    def config_janela(self):
        self.attributes("-fullscreen", True)
        self.protocol("WM_DELETE_WINDOW", self.fechar)


    def layout(self):
        frame_Caixa : Caixa = Caixa(self)

    def run(self):
        self.mainloop()


    def fechar(self):
        res = msg.askokcancel("Fechar", "Tem certeza que deseja fechar?")
        if not res:
            return
        self.destroy()

if __name__  == "__main__":
    root : Janela = Janela()