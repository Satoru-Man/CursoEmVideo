'''
crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista dentro da lista,
ele não será adicionado.
No final serão exibidos todos os valores únicos digitados em ordem crescente.
'''

lista = list()
valor = valorMax = valorMin = 0
# lista.append(int(input('informe um valor: ')))
while True:
    if valor  >= valorMax:
        valorMax = valor
    elif valor <= valorMin:
        valorMin = valor
    valor = int(input('informe um valor: '))
    if valor in lista:
        print(f'valor digitado já existe na lista e não será incluído')
    else:
        lista.append(valor)
    if input('Deseja continuar [s|n] ? ') not in 'Ss':
        break
lista.sort()
print(f'os valores digitados foram {lista}')
