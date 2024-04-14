"""
crie um programa que leia o nome completo de uma pessoa e mostre:
- o nome com letras maiusculas
- o nome ocm letras minusculas
- quantas letras tem o nome sem considerar os espaços
- quantas letras tem o primeiro nome
"""

nomeCompleto = str(input('informe o nome: '))
maiuscula = nomeCompleto.upper()
minuscula = nomeCompleto.lower()
nomeLista = nomeCompleto.strip().split()
""" tamanho = len(nomeLista[0]) + len(nomeLista[1]) + len(nomeLista[2])  """
tamanho = len(nomeCompleto.strip())-nomeCompleto.count(' ')
primeiroNome = nomeLista[0]

print('nomeLista: '.format(nomeLista))
print('nome em maiuscula: {}'.format(maiuscula))
print('nome em minuscula: {}'.format(minuscula))
print('nome Stripado: {}'.format(nomeLista))
print('tamanho sem espacos: {}'.format(tamanho))
print('primeiro nome: {}'.format(primeiroNome))
print('qtde letras 1o nome: {}'.format(len(primeiroNome)))


