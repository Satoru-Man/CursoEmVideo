"""
leia tres nros e informe qual eh o maior e o maior valor digitado
"""
num1 = int(input('informe o primeiro valor: '))
num2 = int(input('informe o segundo valor: '))
num3 = int(input('informe o terceiro valor: '))


# verificando o menor
nroMenor = num1
if num2 < num1 and num2 < num3:
    nroMenor = num2
if num3 < num1 and num3 < num2:
    nroMenor = num3


# verificando o maior
nroMaior = num1
if num2 > num1 and num2 > num3:
    nroMaior = num2
if num3 > num1 and num3 > num2:
    nroMenor = num3

print('o menor valor digitado foi: {}'.format(nroMenor))
print('o maior valor digitado foi: {}'.format(nroMaior))
