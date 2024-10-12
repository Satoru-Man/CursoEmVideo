'''
faça um programa que leia 5 valores numéricos e guarde-os numa lista.
Ao final, mostre qual foi o maior e o menor valor digitado e as
respectivas posições na lista
'''

lista = []
lista.append(input('digite o valor 1: '))
lista.append(input('digite o valor 2: '))
lista.append(input('digite o valor 3: '))
lista.append(input('digite o valor 4: '))
lista.append(input('digite o valor 5: '))

print(f'antes do sort: {lista}')
lista.sort()
print(f'depois do sort: {lista}')

print(f'o maior valor digitado foi: {lista[-1]} na posição {lista.index(lista[-1])}')
print(f'o menor valor digitado foi: {lista[0]} na posição {lista.index(lista[0])}')

# ou
print(f'o maior valor digitado foi: {max(lista)} na posição {lista.index(max(lista[-1]))}')
print(f'o menor valor digitado foi: {min(lista)} na posição {lista.index(min(lista[0]))}')


