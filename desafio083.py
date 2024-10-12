'''
crie um programa onde o usuário digite uma expressão qualquer
que use parênteses (). Se programa deverá analisar se a expressão
está com os parênteses abertos e fechados na ordem correta.
'''
from itertools import count

lista1 = []
lista2 = []
expressao = str(input('digite algo, usando parênteses (): '))

for i in range(len(expressao)):
    if expressao[i] == '(':
        lista1.append(expressao[i])
    elif expressao[i] == ')':
        lista2.append(expressao[i])

if len(lista1) == len(lista2) and len(lista1)>0:
    print('digitado corretamente')
else:
    print('faltou algum parênteses no texto')

aberto = expressao.count('(')
fechado = expressao .count(')')
if aberto == fechado:
    print('digitado corretamente')
else:
    print('faltou algum parênteses no texto')