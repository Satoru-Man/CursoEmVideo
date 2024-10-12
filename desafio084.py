'''
faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre:
A) quantas pessoas foram cadastradas
B) uma listagem com as pessoas mais pesadas
C) uma listagem com as pessoas mais leves
'''

pessoas = []
leves = []
pesadas = []
dado = []
pesoMedio = 0

while True:
    dado.append(input('Informe o nome: '))
    dado.append(int(input('Informe o peso: ')))
    pessoas.append(dado[:])
    pesoMedio = pesoMedio + dado[1]
    dado.clear()
    if input('Deseja continuar S-N: ') not in 'Ss':
        break

print(pessoas)
print(pessoas[0][0])
print(pessoas[0][1])

print(len(pessoas))

pesoMedio = int(pesoMedio / (len(pessoas) + 1))
print(f'peso médio = {pesoMedio}')

for i,p in enumerate(pessoas):
    if p[1] >= pesoMedio:
        pesadas.append(p[0])
        pesadas.append(p[1])
    else:
        leves.append(p[0])
        leves.append(p[1])

print(f'A) foram cadastradas {len(pessoas)} pessoas')
print(f'B) as pessoas mais pesadas foram {pesadas}')
print(f'C) as pessoas mais leves foram {leves}')

