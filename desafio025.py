"""
crie um programa que leia o nome de uma pessoa e diga se ela
tem "SILVA" no nome informado
"""
nome = input('Informe um nome completo: ')
temSILVA = nome.upper().find('SILVA')
print(temSILVA)

print('Tem "SILVA" no nome informado: {}'.format(temSILVA>-1))

' ou '

print('tem SILVA no nome: {}'.format('silva' in nome.lower()))
