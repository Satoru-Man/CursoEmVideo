"""
refazer o exercicio 35
acrescentando o recurso de mostrar que tipo de
triangulo e formado
- equilatero: todos os lados sao iguais
- isosceles: dois lados iguais
- escaleno: todos os lados sao diferentes
"""

r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))

triangulo = r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2)
print(triangulo)
print('dados formam um triangulo') if triangulo else print('dados nao formam um triangulo')
if triangulo:
    if r1 == r2:
        if r1 == r3:
            print('triangulo equilatero')
        else:
            print('triangulo isosceles')
    else:
        if r1 == r3:
            print('triangulo isosceles')
        else:
            print('triangulo escaleno')
else:
    print('dados na formam um triangulo')
