"""
escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80KM/hr mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$ 7.00 por cada KM acima do limite.
"""

vloc = int(input('Informe a velocidade em KM/hr: '))
multa = float((vloc - 80) * 7)
if vloc > 80:
    print('Sua velocidade eh {} KM/hr e voce foi multado em R$ {:.2f}'.format(vloc, multa))
else:
    print('Sua velocidade eh {} KM/hr, inferior ou igual ao limite de 80KM/hr'.format(vloc))


