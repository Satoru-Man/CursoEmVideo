"""
crie um programa que leia vários números inteiros pelo teclado.
No final mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores.
"""

nro = quant = soma = media = mario = menor = 0
resp = 'S'

while resp in 'Ss':
    nro = int(input('Digite um nro: '))
    soma += nro
    quant += 1
    if quant ==1:
        maior = menor = nro
    else:
        if nro > maior:
            maior = nro
        if nro < menor:
            menor = nro
    resp = str(input('Deseja continuar [S, N]: ')).upper().strip()[0]
media = soma / quant
print(f'Fim. Qtde digitados: {quant} e média: {media}')