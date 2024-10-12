'''
crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.
'''

lista = []
pares = []
impar = []

for i in range(7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impar.append(num)
pares.sort()
impar.sort()

lista.append(pares)
lista.append(impar)

print(f'Valores pares digitados: {lista[0]}')
print(f'Valores impares digitados: {lista[1]}')
