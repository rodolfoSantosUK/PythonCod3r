#!/usr/local/bin/python3

class Animal:

    @property
    def capacidade(self):
        return ('dormir', 'comer','beber')

class Homem(Animal):

        @property
        def capacidade(self):
            return super().capacidade + ('amar', 'falar', 'estudar')

class Aranha(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ('fazer tela', 'andar pelas paredes' )

class HomemAranha(Aranha, Homem):
    @property
    def capacidade(self):
        return super().capacidade + \
               ('bater em bandidos', 'atirar teia entre predios')


if __name__ == '__main__':

    john = Homem()
    print(f'John {john.capacidade}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidade}')    

    peter = HomemAranha()
    print(f'Peter: {peter.capacidade}')