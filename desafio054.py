'''
crie um programa que leia o ano de nascimento
de sete pessoas. No final mostre quantas
pessoas ainda não atingiram a maioridade
e quantas já são maiores de idade.
maior de idade = 21
'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input('em que ano a {}a pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else:
        totmenor +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))


"""
idade = atual - nasc

if idade >= 21:
    print('Essa pessoa é maior')
else:
    print('Essa pessoa é menor')
idade = {}
maior21 = menor21 = 0

for c in range(0,7):
    idade[c] = int(input(f"informe o ano de nascimento da pessoa {c+1}: "))
    if idade[c] > 21:
        maior21 = maior21 + 1
    else:
        menor21 = menor21 + 1
print(f"{maior21} pessoa(s) são maiores que 21 anos")
print(f"{menor21} pessoa(s) são menores que 21 anos")
"""