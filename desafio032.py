"""
leia um ano e informe se este ano eh bissexto ou nao
"""
from datetime import date
ano = int(input('informe o ano: '))
if ano == 0:
    ano = date.today().year

bissexto = False
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} eh BISSEXTO'.format(ano))
else:
    print('O ano {} NAO eh Bissexto'.format(ano))
