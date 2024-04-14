"""
pergunte a distancia de uma viagem em K.
Calcule o preco da passagem,
cobrando R 0.50 por KM para viagens de ateh 200KM e
R$ 0.45 para viagens mais longas
"""

distancia = int(input('informe a distancia: '))
preco = 0.00
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('A distancia eh de {} e o preco da viagem eh de R$ {:.2f}'.format(distancia, preco))
"""if distancia > 200:
    preco = (distancia) * 0.45
else:
    preco = (distancia) * 0.50
    
print('A distancia eh de {} e o preco da viagem eh de R$ {:.2f}'.format(distancia, preco))
"""