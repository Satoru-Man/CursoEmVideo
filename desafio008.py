# programa que leia um nro em metros e de suas medidas em centimetros e milimetros

mts = float(input('informe um nro: '))
cent = mts * 100
milim = mts * 1000
print('o nro em metros: {}, em centimetros: {:.0f} e em milimetros: {}'.format(mts,cent, milim))
