#!/usr/local/bin/python3

from abc import ABCMeta, abstractproperty

class Humano(metaclass=ABCMeta):

    especie = 'Homo Sapiens'

    def __init__(self, nome, idade):
        self.nome= nome
        self.idade = idade

    @abstractproperty
    def inteligente(self):
        pass



if __name__ == '__main__':
