'''
valor = bool(input('Digite um valor: '))
print(type(valor))

print(ceil(3.14))
# 4

print(ceil(-3.14))
# -3

print(f'O valor arredondado é {ceil(3.14)}')
# O valor arredondado é 4

print(f'O valor arredondado é {ceil(-3.14)}')
# O valor arredondado é -3
'''
from math import ceil, floor

n1 = float(input('Informe n1: '))
n2 = float(input('Informe n2: '))
s = n1 + n2
print(f'a soma de n1 + n2 é ceil()  = {ceil(s):.2f}'.format(s))
print(f'a soma de n1 + n2 é floor() = {floor(s):.2f}'.format(s))
print('a soma de n1 + n2 é = {:.2f}'.format(s))

