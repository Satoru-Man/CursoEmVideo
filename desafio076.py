'''
crie um programa que tenha uma tupla unica
com nomes de produtos e seus respectivos preços na sequência

No final mostre uma listagem de preços,
organizando os dados em forma tabular
'''

produtos = ('abacate', 1.80, 'banana', 1.30, 'abacaxi', 3.00, 'mamão',2.95)
print('*',20)
print('PRODUTOS \ PREÇOS')
for pos, tupla in enumerate(produtos):
    print(f'{pos}: {tupla}, {produtos[pos+1]}')
print('fim')