"""
pergunte o salario de um funcionaro e calculoe o valor de seu aumento
para salarios superiores a R$ 1250.00 calcule um aumento de 10%
para salarios inferiores ou iguais o aumento eh de 15%
"""
salario = float(input('informe o salario: '))
if salario > 1250.00:
    salario = salario + (salario * 10 / 100) # salario = salario * 1.10
    print('O aumento serah de 10% e o salario novo sera de R$ {:.2f}'.format(salario))
else:
    salario = salario + (salario * 15 / 100) # salario = salario * 1.15
    print('O aumento serah de 15% e o salario novo sera de R$ {:.2f}'.format(salario))
