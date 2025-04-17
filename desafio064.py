"""
crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor '999', que é a condição de parada.
No final mostre quantos números foram digitados e qual a soma entre eles, desconsiderando o flag.
"""

total = cont = nro = 0
nro = int(input('informe um nro ou 999 para parar: '))
while nro != 999:
    total += nro
    cont += 1
    nro = int(input('informe um nro ou 999 para parar: '))
print(f'Fim: Soma={total} Qtde digitados: {cont}')
