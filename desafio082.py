'''
crie um programa que vai ler vários números e colocá-los em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores impares digitados, respectivamente.
ao final, mostre o conteúdo das três listas geradas.
'''

lista0 = []
lista1 = [] # pares
lista2 = [] # impares

while True:
    num = int(input('Digite um valor: '))
    lista0.append(num)
    if input('deseja continuar ') not in 'sS':
        break

for i in range(len(lista0)):
    num = lista0[i]
    print(f'num={num} e {num % 2}')
    if num % 2 == 0:
        lista1.append(num)
    else:
        lista2.append(num)

print(lista0)
print(lista1)
print(lista2)
