from pathlib import Path
import sqlite3


class Historico:
    def __init__(self, operacao : str, valor : float, id : int = None):
        self._id : int = id
        self._operacao : str = operacao.title().strip()
        self._valor : float = valor


    @property
    def operacao(self):
        return self._operacao
    
    @property
    def valor(self):
        return self._valor


if __name__ == "__main__":

        
    def realizar_registro(historico : Historico):
        local : Path = Path.cwd() / "database/database.db"
        with sqlite3.connect(local) as conn:
            cursor : sqlite3.Cursor = conn.cursor()    
            data : tuple = (historico.operacao, historico.valor)
            cursor.execute("INSERT INTO historico (operacao, valor)  VALUES (?, ?)", data)
            conn.commit()

            return "Historico atualizado."

    def buscar_registros() -> sqlite3.Row:
        local : Path = Path.cwd() / "database/database.db"
        with sqlite3.connect(local) as conn:
            conn.row_factory = sqlite3.Row
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT id, valor, operacao FROM historico")
            registros : sqlite3.Row = cursor.fetchall()

            return registros


    # historico : Historico = Historico("Entrada", 100)
    # print(realizar_registro(historico))


    registros = buscar_registros()

    for row in registros:
        print(dict(row))
