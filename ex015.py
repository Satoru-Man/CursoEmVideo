# pergunte a qtde de kilometros rodados por um carro alugado
# e pergunte a qtde de dias desse aluguel
# calcule o preco a pagar pelo aluguel, considerando
# R$ 60,00 por KM rodado e R$ 0.15 por Km rodado

km = float(input('Informe a qtde de Km rodados: '))
dias = int(input('informe a qtde de dias do aluguel: '))
preco = float((dias * 60.00) + (km * 0.15))

print('O valor a pagar pelo aluguel do carro eh: R$ {:.2f}'.format(preco))
