from math import pi


class Calculo():

    def __init__(self):
        self.pi = pi
        self.raio = None

    def circulo (self, raio):
        return self.pi * float(raio) ** 2

if __name__ == '__main__':
    calculo = Calculo()
    raio = input('Informe o raio : ')
    area = calculo.circulo(raio)
    print('Área do círculo ', area)