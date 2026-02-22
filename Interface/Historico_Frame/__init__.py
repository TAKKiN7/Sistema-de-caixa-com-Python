from customtkinter import CTkFrame, CTkToplevel, CTkButton
from tkinter.ttk import Treeview, Style


class Historico_Treeview(Treeview):
    def __init__(self, root):
        super().__init__(root, columns=("Valor", "Operação", "Data"), show="headings")
        self.layout()


    def layout(self):
        self.heading("Valor", text="Valor", anchor="w")
        self.heading("Operação", text="Opereção", anchor="w")
        self.heading("Data", text="Data", anchor="w")

        for c in range(100):
            self.insert("", "end", values=(c, "Entrada", "22/02/2026")) # Somente um teste antes de implementar historico no banco de dados

        #self.pack(fill="both", expand=True)
        self.place(relx=0, rely=0.1, relwidth=1, relheight=.9)
    

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
            bordercolor="red",
            borderwidth=3
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
            relief="flat"
        )

        estilo.map(
            "Treeview.Heading",
            background=[("selected", "BLACK")],
            foreground=[("selected", "WHITE")]
        )