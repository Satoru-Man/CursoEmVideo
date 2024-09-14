'''
desenvolva um programa que leia quatro valores pelo teclado
e guarde-os numa tupla. No final mostre:
A) quantas vezes apareceu o nro 9
B) em que posição foi digitado o primeiro valor 3
C) quais foram os numeros pares
'''

tupla = ()
for i in range(4):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        pares = (valor)
    tupla = tupla + valor

print(tupla)
print(f'A) o nro 9 aparece {} vezes na tupla')
print(f'B) o primeiro valor 3 foi digitado na posição {tupla.index(3)}')
print(f'C) os nros pares foram {pares}')