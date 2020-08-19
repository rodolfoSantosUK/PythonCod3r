#!usr/local/bin/python3

class RGB:

    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1] # itera a partir do último

    def __iter__(self):
        return self # retorna o próprio objeto, pois ele é um iterator por conta da implementação do next

    def __next__(self): # sobreescrevendo o método next
        try:
            return self.cores.pop() # pop pega o último da lista
        except IndexError:
            raise StopIteration()

if __name__ == '__main__' :
    cores = RGB()

    print(next(cores))
    print(next(cores))
    print(next(cores))

    try:
        print(next(cores))
    except StopIteration:
        print('Não há mais o que iterar')

    for cor in RGB():
        print()
        print(cor)




