'''
crie um programa que vai gerar cinco numeros aleatórios e
colocá-los em uma tupla
Depois disso mostre a listagem dos numeros gerados e
também indique o menior e o maior valor que estão na tupla
'''

from random import randint
'''
# Gerar cinco números aleatórios e armazená-los em uma lista
numeros = [randint(0, 10) for _ in range(5)]

# Converter a lista em uma tupla
tupla = tuple(numeros)
# tupla = (numeros)
'''
tupla = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
# Exibir a tupla
print("Números gerados:", tupla)

# Encontrar e exibir o menor e o maior valor
menor = min(tupla)
maior = max(tupla)

print("Menor valor:", menor)
print("Maior valor:", maior)
