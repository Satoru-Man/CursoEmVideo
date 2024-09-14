'''
faça um programa que mostre a tabuada de vários nros,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o nro solicitado for negativo.
'''

nro = 0
while True:
    nro = int(input('Digite um nro para ver sua tabuada: '))
    if nro < 0:
        break
    print('-' * 30)
    print(f'Tabuada do nro {nro}:')
    print('-' * 30)
    for i in range (1,11):
        mult = nro * i
        print(f'{nro} x {i:>2} = {mult:2}')
    print('-' * 30)
print('Fim.')