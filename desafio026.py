"""
crie um programa que leia uma frase qualquer e mostre:
quantas vezes aparece a letra "A"
em que posicao a letra "A" aparece a 1a vez
em que posicao ela aparece pela ultima vez
"""
frase = input('Digite uma frase qualquer: ').strip()
qtdeA = frase.upper().count('A')
primeiroA = frase.upper().find('A')
""" frase.upper().startswith('A') """
"""frase.upper().find('A')"""
ultimoA = frase.upper().rfind('A')
print('A letra "A" aparece {} vezes na frase digitada'.format(qtdeA))
print('A letra "A" aparece primeiro na posicao {} '.format(primeiroA))
print('A letra "A" aparece por ultimo na posicao {} '.format(ultimoA))
N