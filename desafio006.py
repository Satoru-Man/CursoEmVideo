# crie um algoritmo que leia um nro e mostre o seu dobro, triplo e raiz quadrada

from math import sqrt
num = float(input('Informe um nro: '))
print('seu nro digitado foi: {}'.format(num))
num2x = num * 2
num3x = num * 3
numsqrt = num ** (1/2)
print('o dorbo do nro: {} \no triplo do nro: {} \na raiz quadrada do nro: {:.2f}'.format(num2x, num3x, numsqrt))
print('e a raiz quadrada do nro (Sqrt): {:.2f}'.format(sqrt(num)))
