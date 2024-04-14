"""
leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
cada segmento de reta tem que ser menor que a soma do comprimento das outras duas retas
r1 < (r2 + r3)
"""
r1 = float(input(' reta 1: '))
r2 = float(input(' reta 2: '))
r3 = float(input(' reta 3: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Essas tres retas formam um triangulo')
else:
    print('Essas tres retas NAO formam um triangulo')
