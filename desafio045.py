"""
crie um programa que faca o computador jogar jokenpo
- pedra
- papel
- tesoura
papel > pedra
pedra > tesoura
tesoura > papel
"""
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador  = randint(0, 2)
print('O computador escolheu {}' .format(itens[computador]))
print('''Suas Opcoes: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual eh a jogada? '))

print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
sleep(1/2)

print('-='*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador    jogou {}'.format(itens[jogador]))
print('-='*20)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada invalida!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada invalida')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')