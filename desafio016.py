# pedir um nro Real e mostrar a porcao inteira desse nro

import math

nro = float(input('informe um nro: '))
decimal = math.modf(nro)
inteiro = int(nro) #math.trunc(nro)
print('o nro informado foi {} e sua parte decimal eh: {} e o inteiro eh: {}'.format(nro, decimal, inteiro))
