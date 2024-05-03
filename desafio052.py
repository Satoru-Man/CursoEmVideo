'''
faca um programa que leia um numero inteiro
e diga se ele eh ou nao um nro primo.
OBS: nros primos sao aqueles que sao divididos por 1 e por ele mesmo
'''

num = int(input('informe um numero: '))

if (num % 1) == 0 and (num % num) == 0:
    print('o numero informado eh primo')
else:
    print('o numero informado nao eh um nro primo')
