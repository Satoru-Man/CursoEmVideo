"""
a conf. nacional de natacao precisa de um programa que
leia o ano de nascimento de um atleta e mostre a sua categoria de
acordo com a idade:
- ate 9 anos: Mirim
- ate 14 anos: infantil
- ate 19 anos: junior
- ate 20 anos: senior
- acima 20 anos: master
"""
from datetime import date
anoS = date.today().year
anoI = int(input('informe o ano do atleta: '))
lim = anoS - anoI

print('a idade do atleta eh de {}'.format(lim))
if lim <= 9:
    print('categoria mirim')
elif lim <= 14:
    print('categoria infantil')
elif lim <= 19:
    print('categoria junior')
elif lim <= 20:
    print('categoria senior')
else:
    print('categoria master')
