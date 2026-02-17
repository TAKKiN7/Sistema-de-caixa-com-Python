from database.database import Banco
from Interface import Janela


banco: Banco = Banco()
caixa = banco.obter_caixa()
print(caixa.saldo)

root : Janela = Janela(caixa)