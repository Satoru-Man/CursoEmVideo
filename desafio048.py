'''
faca um programa que calcule a soma
entre todos os numeros IMPARES que
sao multiplos de tres e que se encontram
no intervalo de 1 ate 500
'''
soma = 0
for c in range(0,500):
    if (c % 2) > 0:
        soma = soma + c
print('O total da soma dos nros impares eh {}'.format(soma))
