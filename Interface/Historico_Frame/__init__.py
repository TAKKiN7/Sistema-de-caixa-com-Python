from customtkinter import CTkFrame, CTkToplevel, CTkButton
from tkinter.ttk import Treeview, Style
import sqlite3
from pathlib import Path


class Historico_Treeview(Treeview):
    def __init__(self, root):
        super().__init__(root, columns=("Id", "Valor", "Operação"), show="headings")
        self.layout()


    def layout(self):
        self.heading("Valor", text="  Valor", anchor="w")
        self.heading("Operação", text="Opereção", anchor="w")
        self.heading("Id", text="Id", anchor="w")
        self.tag_configure("vermelho", foreground="red")
        self.tag_configure("verde", foreground="green")

        registros = self.buscar_registros()
        if registros:
            for registro in registros:
                historico : dict = dict(registro)
                operacao = historico.get("operacao")
                if operacao.lower() == "saída":
                    saldo : str = str(f"-{historico.get("valor"):.2f}").replace(".", ",")
                    self.insert("","end", values=(historico.get("id"), saldo, historico.get("operacao")), tags=("vermelho",))
                else:
                    saldo : str = str(f" {historico.get("valor"):.2f}").replace(".", ",")
                    self.insert("","end", values=(historico.get("id"), saldo, historico.get("operacao")), tags=("verde",))

        self.place(relx=0, rely=0.1, relwidth=1, relheight=.9)
    
    
    def buscar_registros(self) -> sqlite3.Row:
        local : Path = Path.cwd() / "database/database.db"
        with sqlite3.connect(local) as conn:
            conn.row_factory = sqlite3.Row
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT id, valor, operacao FROM historico")
            registros : sqlite3.Row = cursor.fetchall()

            return registros
        



class Historico(CTkToplevel):
    def __init__(self, root):
        super().__init__(root)
        self.configure(bg_color="BLACK", fg_color="BLACK")
        self.config()
        self.layout()


    def config(self):
        self.grab_set()
        larguraT = self.winfo_screenwidth()
        alturaT = self.winfo_screenheight()
        self.overrideredirect(True)
        self.geometry(f"520x330+{int((larguraT / 2) - (520 / 2))}+{int((alturaT / 1.65))}")

    
    def layout(self):
        fecharB : CTkButton = CTkButton(self, text="Fechar", fg_color="RED", corner_radius=0,
                                        command=self.fechar,border_width=2, border_color="BLACK",
                                        hover_color="#5c0a12")
        fecharB.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.style()
        tree : Treeview = Historico_Treeview(self)


    def fechar(self):
        self.destroy()

    def style(self):
        estilo = Style()
        estilo.theme_use("default")

        estilo.configure(
            "Treeview",
            foreground="WHITE",
            background="#1C2238",
            fieldbackground="#1C2238",
            bordercolor="BLACK",
            borderwidth=1,
            relief="RIDGE"

        )

        estilo.map(
            "Treeview",
            background=[("selected", "BLACK")],
            foreground=[("selected", "white")]
        )

        estilo.configure(
            "Treeview.Heading",
            background="#1C2238",
            foreground="white",
            borderwidth=1,
            bordercolor= "BLACK",
            relief="RIDGE"
        )

        estilo.map(
            "Treeview.Heading",
            background=[("selected", "BLACK")],
            foreground=[("selected", "WHITE")]
        )