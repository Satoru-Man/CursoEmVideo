'''
crie um programa que leia o nome e o preço de vários produtos.
O pgm deverá perguntar se o usuário vai continuar ou não.
No final mostre:
a) qual o total gasto na compra
b) quantos produtos custam mais de 1000,00
c) qual é o nome do produto mais barato
'''

nome = produtomaisbarato = ''
total = maisbarato = 0.00
preco = 0.00
continua = ''
maiscaros = 0

while continua != 'N':
    nome = input('Informe o nome do produto: ')
    preco = float(input('informe o valor do produto: '))
    total = total + preco
    if preco > 1000.00:
        maiscaros += 1
    elif preco < maisbarato or maisbarato == 0.00:
        produtomaisbarato = nome
        maisbarato = preco
    continua = input('Deseja continuar S ou N: ').strip().upper()[0]

print(f'O total gasto na compra: {total}')
print(f'Produtos mais caros que 1000,00: {maiscaros}')
print(f'Nome do produto mais barato: {produtomaisbarato}')