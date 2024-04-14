"""
ler dois nros inteiros e compara-los
mostrando a mensagem:
- o primeiro valor eh maior
- o segundo valor eh maior
- nöao existe valor maior, os dois nros sao iguais
"""
n1 = int(input('Informe o nro 1: '))
n2 = int(input('informe o nro 2: '))

if n1 > n2:
    print('o nro {} e maior que o nro {}'.format(n1,n2))
elif n2 > n1:
    print('o nro {} e maior que o nro {}'.format(n2,n1))
else:
    print('\033[2:41m os dois nros sao iguais! \033[m')

