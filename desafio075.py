'''
desenvolva um programa que leia quatro valores pelo teclado
e guarde-os numa tupla. No final mostre:
A) quantas vezes apareceu o nro 9
B) em que posição foi digitado o primeiro valor 3
C) quais foram os numeros pares
'''
from itertools import count

nros = (int(input('Digite o valor 1: ')),
        int(input('Digite o valor 2: ')),
        int(input('Digite o valor 3: ')),
        int(input('Digite o valor 4: ')))

print(f'A) O número 9 aparece {nros.count(9)} vezes.')
if 3 in nros:
    print(f'B) O número 3 aparece inicialmente na posição {nros.index(3)+1}')
else:
    print(f'O valor 3 não foi digitado.')
print(f'C) Os números pares são: ', end='')
for n in nros:
    if n % 2 == 0:
        print(n, end=' ')

print('\nfim')

''' tupla1 = ()
tupla2 = ()
noves = 0
for i in range(4):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        pares = valor
    elif valor == 0:
        noves =+ 1
    tupla1 = tupla1 + tuple(int(valor)
    #tupla = tupla.append(valor)

print(tupla)
print(f'A) o nro 9 aparece {noves} vezes na tupla')
print(f'B) o primeiro valor 3 foi digitado na posição {tupla.index(3)}')
print(f'C) os nros pares foram {pares}')
'''