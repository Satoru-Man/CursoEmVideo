'''
faça um programa que jogue par ou impar.]
O jogo será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou ao final do jogo.
valor e se par ou impar
'''

import random

parimpar = 'Pp'
comp = usr = vitorias = 0
while parimpar in 'PpIi':
    parimpar = input('Informe se [P]ar ou [I]mpar: ')
    usr = int(input('Informe o nro: '))
    comp = random.randint(usr,1000)
    print(f'Usuário: {usr} e Computador: {comp}')
    if parimpar in ('Pp'):
        if (usr % 2 == 0) and (comp % 2 == 0):
            print(f'O usuário ganhou escolhendo PAR.')
        elif (usr % 2 > 0) and (comp % 2 > 0):
            print(f'O computador ganhou.')
            break
        else:
            print('ninguém ganhou 1.')
    else:
        if (usr % 2 == 0) and (comp % 2 == 0):
            print(f'O computador ganhou escolhendo PAR.')
            break
        elif (usr % 2 > 0) and (comp % 2 > 0):
            print(f'O usuário ganhou.')
        else:
            print('ninguém ganhou 2,')
print('Fim')


'''
from randon import randint

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('[P]ar ou [Í]mpar ?: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print(f'Você venceu')
            v += 1
        else:
            print('você Perdeu')
            break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você venceu')
                v += 1
            else:
                print('Você perdeu')
                break
        print('Vamos jogar novamente...')
    print(f'Você venceu {v} vezes.')   
'''