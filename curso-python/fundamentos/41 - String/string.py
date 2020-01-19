nome = "Ana Paula"

print(nome[4:]) # a partir da posição 4
print(nome[-3]) # pega elementos da direita pra esquerda 
print(nome[:3]) # o indice 3 não é levado em conta
print(nome[2:5]) # Nao considera o 5 


numeros = '1234567890'
print(numeros[::])
print(numeros[::2]) # Vai pegar todos os numeros e vai usar step de 2 em 2
print(numeros[::-1]) # retorna o valor invertido


frase= "Python é uma linguagem excelente"
print('py' not in frase) 
'ing' in frase
len(frase)

frase.lower()

frase.split()