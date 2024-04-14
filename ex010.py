# leia um valor e informe quanto em dolares tem baseado nesse valor
# peca a cotacao do dia
dolar = float(input('Informe o valor do dolar: '))
real = float(input('Informe o valor a converter: '))
print('o valor da cotacao do dolar informado foi: {:.2f}'.format(dolar))
print('o valor em reais foi R${:.2f} que convertido eh: R${:.2f}'.format(real, real / dolar))
print('125.32 / 3.27 = {:.2f}'.format(125.32 / 3.27))
