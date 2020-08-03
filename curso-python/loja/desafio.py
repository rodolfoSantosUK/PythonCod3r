#!/usr/local/bin/python3

from datetime import datetime
from loja import Cliente, Vendedor, Compra

cliente = Cliente('Maria Lima', 44)
vendedor = Vendedor('Pedro Garrido', 36, 5000)

compra1 = Compra(cliente, datetime.now(), 512)
compra2 = Compra(cliente, datetime(2018,6,4), 256)

cliente.registrar_compras(compra1)
cliente.registrar_compras(compra2)

print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adult() else '')
print(f'Vendedor: {vendedor}')


valor_total = cliente.total_compras()
qtde_compras = len(cliente.compras)

print(f'Total: {valor_total} em {qtde_compras} compras')


