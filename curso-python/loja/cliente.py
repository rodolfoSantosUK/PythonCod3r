from .pessoa import Pessoa


def get_data(compra):
    return compra.data

class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.minhasCompras = []

    def registrar_compras(self, compra):
        self.minhasCompras.append(compra)

    def get_data_ultima_compra(self):
        return None if not self.minhasCompras else \
            sorted(self.minhasCompras, key=lambda c : c.data )[-1].data # pegando o ultimo elemento da lista

    def total_compras(self):
        total = 0
        for compra in self.minhasCompras:
            total += compra.valor
        return total

