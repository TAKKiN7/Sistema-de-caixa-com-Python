from database.database import Banco
from models.Caixa import Caixa
from Interface import Janela


# ojb Banco, responsavel por criar o ".db" e criar as informaçães do Caixa
banco : Banco = Banco()

# obj Caixa criado pelo banco apos obter as informações do caixa no ".db"
caixa : Caixa = banco.obter_caixa()

# inicializa a parte gráfica do Caixa
root : Janela = Janela(caixa, banco)