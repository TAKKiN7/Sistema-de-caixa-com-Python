import sqlite3
from pathlib import Path
from models.Caixa import Caixa
from models.Historico import Historico



class Banco:
    def __init__(self):
        self.database_dir()
        self.create_db_arq(self._caminho)
        self.create_table()


    def database_dir(self):
        local : Path = Path.cwd()
        self._caminho : Path = Path(local / "database")
        self._caminho.mkdir(exist_ok=True)


    def create_db_arq(self , caminho):
        database_arq : Path = Path(caminho / "database.db")
        database_arq.touch(exist_ok=True)

        self._banco : str = str(database_arq)
    

    def create_table(self):
        with sqlite3.connect(self._banco) as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS gelados (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), saldo REAL)")
            cursor.execute("CREATE TABLE IF NOT EXISTS historico (id INTEGER PRIMARY KEY AUTOINCREMENT, operacao VARCHAR(100), valor REAL)")
            conn.commit()
            self.garantir_caixa()

    def garantir_caixa(self):
        if not self.caixa_existe():
            with sqlite3.connect(self._banco) as conn:
                cursor : sqlite3.Cursor = conn.cursor()
                cursor.execute("INSERT INTO gelados (nome, saldo) VALUES (?, ?)", ("NT_GELADOS", 0))
                conn.commit()
    
    def caixa_existe(self) -> bool:
        with sqlite3.connect(self._banco) as conn:
            conn.row_factory = sqlite3.Row
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT id, nome FROM gelados WHERE id = ?", (1, ))
            resultado = cursor.fetchone()

            return resultado if resultado else None
    

    def obter_caixa(self) -> Caixa:
        with sqlite3.connect(self._banco) as conn:
            conn.row_factory = sqlite3.Row
            cursor : sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT id, nome, saldo FROM gelados WHERE id = ?", (1, ))
            resultado : dict = dict(cursor.fetchone())

            id = resultado.get("id")
            nome = resultado.get("nome")
            saldo = resultado.get("saldo")

            return Caixa(id=id, nome=nome, saldo=saldo)
    
    def realizar_registro(self, historico : Historico):
        with sqlite3.connect(self._banco) as conn:
            cursor : sqlite3.Cursor = conn.cursor()    
            data : tuple = (historico.operacao, historico.valor)
            cursor.execute("INSERT INTO historico (operacao, valor)  VALUES (?, ?)", data)
            conn.commit()

            return "Caixa atualizado."

    
    def atualizar_caixa(self, caixa : Caixa)-> str:
         with sqlite3.connect(self._banco) as conn:
            cursor : sqlite3.Cursor = conn.cursor()
            data : tuple = (caixa.saldo, caixa.id)
            cursor.execute("UPDATE gelados SET saldo = ? WHERE id = ?", data)
            conn.commit()

            return "Caixa atualizado."
