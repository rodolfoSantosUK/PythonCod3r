#!/usr/local/bin/python3

class Humano:

    especie = 'Homo Sapiens'

    def __init__(self, nome, idade):
        self.nome= nome
        self.idade = idade

    @property
    def idade(self, idade):
        return idade

    @idade.seterr
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthal'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habbilis', 'Erectus', 'Sapiens')
        return ('Australopiteco', ) + tuple(f'Homo {adj}' for adj in adjetivos )

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]



if __name__ == '__main__':

    jose = HomoSapiens('Jose')
    jose.idade = 40 #setou setando

    print(f'Nome: {jose.nome} / Idade: {jose.idade}')
