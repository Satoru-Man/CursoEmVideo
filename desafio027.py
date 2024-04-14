"""
faça um programa que leia um nome e mostre separadamente somente o primeiro e o ultimo nome
"""
nomeCompleto = input('informe um nome qualquer: ')
nomeLista = nomeCompleto.split()
tamLista = len(nomeLista)
primeiroNome = nomeLista[0]
ultimoNome = nomeLista[tamLista-1]

print('o primeiro nome eh: {}'.format(primeiroNome))
print('o ultimo nome eh: {}'.format(ultimoNome))
