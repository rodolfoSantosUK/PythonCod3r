from decimal import Decimal, getcontext

print(dir())

print(dir(__builtins__))

Decimal(1) / Decimal(7)

# MUDANDO O CONTEXTO DE PRECISÃO DE CASAS DECIMAIS

getcontext().prec = 4

print(Decimal(1) / Decimal(4))

print(Decimal.max(Decimal(1), Decimal(7)))

