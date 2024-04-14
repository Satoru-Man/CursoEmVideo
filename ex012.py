# calcule um desconto de 5% sobre um produto informado

valorProd = float(input('Informe o valor do produto: '))
desconto = float(valorProd * 0.05)
print('este produto, no valor de {} tem um desconto de 5% {} e seu valor eh de: {:.2f}'.format(valorProd, desconto, (valorProd-desconto)))
