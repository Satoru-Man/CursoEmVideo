'''
faça um programa que ajude um jogador da MEGASENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números,
entre 1 e 60, para cada jogo, adastrando tudo em uma lista composta
'''

from random import randint

qtde = int(input('Quantos jogos deseja? '))
jogos = list(range(qtde))
colunas = []

for i in range(qtde):
    for j in range(6):
        valor = randint(1, 60)
        if valor in colunas:
            j=j-1
        else:
            colunas.append(valor)
    colunas.sort()
    jogos[i] = [colunas[:]]
    colunas.clear()

for i, pos in enumerate(jogos):
    print(f'Jogo {i+1}: {pos}')
