'''
faca um programa que calcule a soma
entre todos os numeros IMPARES que
sao multiplos de tres e que se encontram
no intervalo de 1 ate 500
'''
soma = 0
for c in range(1,501,2):
    if (c % 3) == 0:
        print(c, end=' ')
        soma = soma + c
print('\nO total da soma dos nros impares eh {}'.format(soma))
