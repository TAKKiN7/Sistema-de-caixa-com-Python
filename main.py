from database.database import Banco




banco : Banco = Banco()
caixa = banco.obter_caixa()




caixa.saida(1000)

response = banco.atualizar_caixa(caixa=caixa)
print(response)
caixa.entrada(10000)
caixa.saldo = 0

print(caixa.saldo)