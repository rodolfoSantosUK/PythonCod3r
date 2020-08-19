#!/usr/local/bin/python3
class ClasseSimples:
    contador = 0;

    def __init__(self):
       # self.contar()
       # ou
        self.__class__.contador += 1

    @classmethod
    def contar(cls):
        cls.contador +=1

if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples()]
    print(f' Quantidade de instâncias {ClasseSimples.contador} ')