'''
crie um programa que vai ler vários números e colocá-los em uma lista.
Depois disso mostre:
A) quantos números foram digitados
B) a lista de valores ordenada de forma decrescente;
C) se o valor 5 foi digitado e está ou não na lista
'''

lista = list()
while True:
    if input('Deseja digitar um valor ? [S]im [N]ão: ') in 'Ss':
        lista.append(int(input('Informe o valor: ')))
    else:
        break
print(f'A) foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'B) a lista de valores ordenada é: {lista}')
if lista.index(5)>0:  # ou if 5 in lista:
    tem = ''
else:
    tem = 'não'
print(f'C) o valor 5 {tem} está na lista.')



