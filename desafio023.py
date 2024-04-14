"""
faca um programa que leia um nro de 0 a 9999
e mostre na tela cada um dos digitos separados"""

nro = input('informe um nro de 0 a 9999: ')
nro = nro[:4]
print('unidade: {}'.format(nro[3]))
print('dezena : {}'.format(nro[2]))
print('centena: {}'.format(nro[1]))
print('milhar : {} \n'.format(nro[0]))

' ou '

num = int(nro)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: {} '.format(u))
print('dezena : {}'.format(d))
print('centena: {}'.format(c))
print('milhar : {}'.format(m))