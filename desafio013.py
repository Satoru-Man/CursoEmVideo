# mostrar o salario de um funcionario com 15% de aumento

salarioAnterior = float(input('informe o salario atual: '))
salarioComAumento15 = float(salarioAnterior * 1.15)
# codigo alternativo salarioComAumento15 = salario + (salario * 15 / 100)

print('O salario do funcionario, de {:.2f} tera um aumento de 15%: {:.2f}'.format(salarioAnterior,salarioComAumento15))
