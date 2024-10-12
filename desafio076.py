'''
crie um programa que tenha uma tupla unica
com nomes de produtos e seus respectivos preços na sequência

No final mostre uma listagem de preços,
organizando os dados em forma tabular
'''

produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99)

# Encontrando o comprimento da tupla para controlar o loop
tamanho = len(produtos)

# Imprimindo o cabeçalho da tabela
print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)
print('Produto'.ljust(30), 'Preço')
print('-' * 40)

# Imprimindo os produtos e seus preços
for pos in range(0, tamanho, 2):
    print(f'{produtos[pos]:.<30}', f'R${produtos[pos+1]:>7.2f}')

print('-' * 40)

