'''
crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta.
'''


lista = []
nros1 = []
nros2 = []
nros3 = []

for i in range(9):
    valor = int(input(f'Digite o valor {i}: '))
    if i < 3:
        nros1.append(valor)
    elif i < 6:
        nros2.append(valor)
    else:
        nros3.append(valor)

lista.append(nros1)
lista.append(nros2)
lista.append(nros3)

print(lista)

print('+-+-+-+')
print(f'|{lista[0][0]}|{lista[0][1]}|{lista[0][2]}|')
print(f'+-+-+-+')
print(f'|{lista[1][0]}|{lista[1][1]}|{lista[1][2]}|')
print(f'+-+-+-+')
print(f'|{lista[2][0]}|{lista[2][1]}|{lista[2][2]}|')
