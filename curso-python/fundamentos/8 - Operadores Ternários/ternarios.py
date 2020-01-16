 
its_rainning = True
mensagem = 'Estou com as roupas ' + ('secas', 'molhadas')[its_rainning]

mensagem2 = 'Estou com as roupas ' + ('molhadas ' if its_rainning else ' secas' )

print(mensagem)

print(mensagem2)