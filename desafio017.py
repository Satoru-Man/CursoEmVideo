# dado o comprimento do cateto oposto e cateto adjacente de um triangulo retangulo
# calcular a hipotenusa

# hipotenusa eh igual aa raiz quadrada da soma dos catetos ao quadrado

import math

oposto = float(input('informe o cateto oposto: '))
adjacente = float(input('informe o cateto adjacente: '))
# hipotenusa = math.sqrt(math.sqrt(oposto + adjacente))
# hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
hipotenusa = math.hypot(oposto, adjacente)
print('a hipotenusa eh: {:.2f}'.format(hipotenusa))

