"""
faca um programa que leia o ano de um nascimento
e informe de acordo com sua idade:
- se ele ainda vai se alistar no servico militar
- se e hora de se alistar
- se ja passou o tempo do alistamento

o programa tambem devera mostrar o tempo que falta para ou o tempo que passou
do periodo de alistamento

"""
from datetime import datetime
anoS = datetime.today().year
anoI = int(input('informe o ano de nascimento: '))
idade = anoS - anoI
print('Quem nasceu em {} tem {} anos em {}' .format(anoI, idade, anoS))

if idade == 18:
    print('estah no ano do alistamento')
elif idade > 18:
    saldo = idade - 18
    print('passou do prazo do alistamento')
    print('ja deveria ter se alistado há {} anos'.format(saldo))
    ano = anoS - saldo
    print('seu alistamento foi em {}' .format(ano))
else:
    saldo = 18 - idade
    print('falta tempo para o alistamento')
    print('ainda faltam {} anos para se alistar'.format((saldo)))
    ano = anoS + saldo
    print('seu alistamento será em {}' .format(ano))

# print('Para o ano de alistamento {} o ano informado tem o prazo de {}'.format(anoS, prazo-18))
