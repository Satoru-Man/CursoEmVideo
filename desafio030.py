"""
leia um nro inteiro e mostre na tela
se ele eh PAR ou se eh IMPAR
"""
import math

nro = int(input('informe um nro: '))
print('o nro {} eh PAR'.format(nro)) if (nro % 2) == 0 else print('O nro eh IMPAR')
