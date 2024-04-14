"""
escreva um programa que leia um nro inteiro qualquer e
peca para o usuario escolher qual sera a base de conversao
1 - binario
2 - octal
3 - hexadecimal
"""

nro = int(input('Informe um nro a converter: '))
bas = int(input('''informe a base de conversao: 
1-binario 
2-octal 
3-hexadecimal: '''))

if bas == 1:
    #nroConvertido = bin(nro)
    print('o nro convertido para binario eh: {}'.format(bin(nro)[2:]))
elif bas == 2:
    #nroConvertido = oct(nro)
    print('o nro convertido para octal eh: {}'.format(oct(nro)[2:]))
elif bas == 3:
    #nroConvertido = hex(nro)
    print('o numero convertido para Hexadecimal eh: {}'.format(hex(nro)[2:]))
else:
    print('opcao invalida')

