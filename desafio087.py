'''
Aprimore o desafio anterior: (086 - crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores
lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta. )
Mostre:
A) a soma de todos os valores digitados
B) a soma dos valores da terceira coluna
C) o maior valor da segunda linha
'''

lista = []
nros1 = []
nros2 = []
nros3 = []
soma3aCol = somaTodos = somaPares = maiorValor2aLinha = 0

for i in range(9):
    valor = int(input(f'Digite o valor {i}: '))
    somaTodos = somaTodos + valor
    if valor % 2 ==0:
        somaPares = somaPares + valor
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
for j, pos in enumerate(lista):
    print(f'|{pos[0]}|{pos[1]}|{pos[2]}|')
    soma3aCol = soma3aCol + pos[2]
    if j==1: # linha 2
        if pos[0] >= pos[1] and pos[0] >= pos[2]:
            maiorValor2aLinha = pos[0]
        elif pos[1] >= pos[2]:
            maiorValor2aLinha = pos[1]
        else:
            maiorValor2aLinha = pos[2]

print(f'X) a soma de todos os valores: {somaTodos}')
print(f'A) a soma de todos os valores pares: {somaPares}')
print(f'B) a soma da terceira coluna: {soma3aCol} ')
print(f'C) o maior valor da 2 linha: {maiorValor2aLinha}')

