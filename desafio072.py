''' crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
seu programa deverá ler um numero pelo teclado (entre 0 e 20)
e mostrá-lo por extenso
'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete','dezoito',
           'dezenove', 'vinte')

for i in extenso:
    valor = int(input('Digite um valor entre 0 e 20: '))
    #if valor < 0 or valor > 20:
    if 0 <= valor <= 20:
        print(extenso[valor])
        if input('Deseja continuar? ') not in 'Ss':
            exit(0)
    else:
        print('valor fora do range! Tente novamente')
print('Fim')
