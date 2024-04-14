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

opcaoComp = randint(0,3)
opcaoUser = int(input('informe a opcao:\n'
                      '1 = papel\n'
                      '2 = tesoura\n'
                      '3 = pedra\n'))

compGanha = (opcaoComp == 1 and opcaoUser == 3) or ...

if opcaComp == 1 and opcaoUser ==