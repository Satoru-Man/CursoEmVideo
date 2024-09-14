"""
faça um programa que leia um número qualquer e mostre o seu fatorial
ex: 5 = 5x4x3x2x1=120
"""

from math import factorial
#
print('FORMA 1')
nro = int(input("Informe um nro: "))
f = factorial(nro)
print(f'o fatorial de {nro} é {f}')

#
print('FORMA 2')
fatorial = contador = nro
txt = str(nro) + '!=' + str(nro) + 'x'
while contador > 1:
    fatorial = fatorial * (contador - 1)
    txt = txt + str(contador - 1) + 'x'
    contador -= 1
print(f'{txt} = {fatorial}')

#
print('FORMA 3')
n = int(input('Digite um nro para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c),end='')
    print('x' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))



