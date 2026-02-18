from database.database import Banco
from models.Caixa import Caixa
from Interface import Janela


banco : Banco = Banco()
caixa : Caixa = banco.obter_caixa()
root : Janela = Janela(caixa, banco)