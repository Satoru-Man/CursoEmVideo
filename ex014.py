# converter Celsius em Fahrenheit e vice versa
# 1 grau celsius = ((9*C)/5)+32

c = float(input('informe os graus Celsius: '))
f = ((9*c)/5)+32
# ou f = 9 * c / 5 + 32 porque a orde de precedencia das operacoes eh * ou / e depois + ou -

print('{:.2f} Graus Celsius informado equivalem a {:.2f} graus Fahrenheit'.format(c,f))
