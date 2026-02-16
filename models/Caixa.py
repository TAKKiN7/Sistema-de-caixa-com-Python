from datetime import date



class Caixa:
    def __init__(self, id : int, nome : str, saldo : float):
        self._id = id
        self._nome = nome
        self._saldo = saldo



    @property
    def id(self):
        return self._id
    

    @property
    def nome(self):
        return self._nome

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @saldo.setter
    def saldo(self, value):
        self._saldo = value
    
    @staticmethod
    def valida_valor(valor : float) -> None:
        if valor <=0:
            raise ValueError("Valor de entrada deve ser maior que ZERO")


    def entrada(self, valor : float):
        Caixa.valida_valor(valor=valor)

        self._saldo += valor

    
    def saida(self, valor : float):
        """
        Permite saldo negativo(Controle de débito)
        
        :param self: instancia da classe
        :param valor: valor que será registado com saída
        :type valor: float
        """

        Caixa.valida_valor(valor=valor)
       
        self._saldo -= valor


        


if __name__ == "__main__":
    caixa = Caixa(1, "NT_GELADOS", 0)
    caixa.entrada(100)