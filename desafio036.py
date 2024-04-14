"""
programa para aprovar o emprestimo bancario da compra de uma casa
perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
calcular o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario
ou entao o emprestimo sera negado
"""

valCasa = float(input('Informe o valor da casa: '))
salario = float(input('informe o salario: '))
qtdeAnos = float(input('informe a qtde de anos para os pagamentos: '))

prestacao = valCasa / (qtdeAnos * 12)
minimo = salario * 30 /100
if prestacao <= minimo:
    print('o valor da prestacao sera de {}{:.2f}{}'.format('\033[2;31m', prestacao, '\033[m'))
else:
    print('o valor da prestacao excede 30% do salario! Emprestimo negado.')
