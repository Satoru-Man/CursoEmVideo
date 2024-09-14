'''
crie um programa que vai gerar cinco numeros aleatórios e
colocá-los em uma tupla
Depois disso mostre a listagem dos numeros gerados e
também indique o menior e o maior valor que estão na tupla
'''

from random import randint
tupla = ()
for i in range(5):
    temp = (randint(0, 10))
    tupla = tupla + temp
print(tupla)
print(sorted(tupla)[0])
print(sorted(tupla)[len(tupla)])
