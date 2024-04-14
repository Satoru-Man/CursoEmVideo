"""
elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preco normal e condicao de pagamento:
- a vista dinheiro/cheque: 10% desconto
- a vista no cartao: 5% desconto
- em ate 2x no cartao: preco normal
- 3x ou mais no cartao: 20% jutos
"""
preco = float(input('informe o preco: '))
condicaoPagto = int(input('informe a condicao de pagto: \n'
                          '0 = a vista\n'
                          '1 = a vista no cartao\n'
                          '2 = em ate 2x\n'
                          '3 = em 3x ou mais\n'
                          ''))
precoNovo = 0.00
if condicaoPagto == 0:
    precoNovo = preco - (preco * (10 / 100))
elif condicaoPagto == 1:
    precoNovo = preco - (preco * (5 / 100))
elif condicaoPagto == 2:
    precoNovo= preco
elif condicaoPagto == 3:
    precoNovo = preco + (preco * (20 / 100))
else:
    print('condicao de pagto invalida!')

print('o produto no valor de R$ {} custara R$ {} na condicao escolhida'
      .format(preco, precoNovo))
