'''
crie um programa que leia vário nros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição e parada.
no final mostre quantos nros foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
'''

nro = cont = soma = 0
while True:
    nro = int(input('Digite um nro ou 999 para encerrar: '))
    if nro == 999:
        break
    cont += 1
    soma += nro
print(f'Foram digitados {cont} nros e a soma é {soma}')
