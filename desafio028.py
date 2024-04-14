"""
escreva um programa que faca o computador pensar em um numero inteiro
entre 0 e 5 e peca para o usuario tentar descobrir qual foi numero escolhido pelo computado
o programa devera escrever na tela se o usuario venceu ou perdeu
"""
from random import randint

numComp = randint(0,5)
""" numComp = int(numComp * 10) """
numUsr = int(input('Informe nro que o computador pensou: '))

if numUsr == numComp:
    print('#' * 20)
    print('Voce acertou o nro!')
    print('#' * 20)
else:
    print('Voce errou o nro!')
print('O numero do computador eh: {}'.format(numComp))




