'''
Crie um programa que leia uma frase qualquer
e diga se ela eh um palindromo,
desconsiderando os espacos na frase.
Ex: frases ou palavras que sao iguais se lidas de tras pra frente
APOS A SOPA eh um palindromo, assima como ANA
'''

frase = str(input('Informe uma frase qualquer: '))

print(frase)
for c in range(0,len(frase)):

    print(frase[c])
