# dado um angulo, informar o seno, cosseno e tangente

from math import sin, cos, tan, radians

angulo = radians(float(input('informe o angulo: ')))  # transforma um nro em radianos
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print('o seno do angulo {} eh {:.2f}'.format(angulo, seno))
print('o cosseno do angulo {} eh {:.2f}'.format(angulo, cosseno))
print('a tangente do angulo {} eh {:.2f}'.format(angulo, tangente))
