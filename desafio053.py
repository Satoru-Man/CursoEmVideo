'''
Crie um programa que leia uma frase qualquer
e diga se ela eh um palindromo,
desconsiderando os espacos na frase.
Ex: frases ou palavras que sao iguais se lidas de tras pra frente
APOS A SOPA eh um palindromo, assima como ANA
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona

programa apresentado pelo curso eh:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palilndromo!')
print(junto, inverso)

***** OU sendo mais sintético *****

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palilndromo!')
print(junto, inverso)

'''

frase = str(input('Informe uma frase qualquer: '))

print(frase)
palindromo = True
texto = f"A frase '{frase}' éh um palindromo"
frase = frase.replace(' ','')
esarf = ''

tamanho_frase = len(frase)

for c in range(0, len(frase)):
    esarf = esarf + frase[(tamanho_frase - c) - 1]
    if frase[c] != frase[(tamanho_frase - c)-1]:
        palindromo = False
        texto = f"A frase '{frase}' não éh um palindromo"
print(esarf)
print(texto)
