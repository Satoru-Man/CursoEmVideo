'''
crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort)
NO final mostre a lista ordenada na tela.
'''


lista = list()
menor = 0
pos = 0
ant = 0
for i in range(0, 5):
    num = int(input('digite um valor: '))
    if i ==0 or num >= lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos <= len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(lista)



'''
    #for j in range(len(lista) - 1, -1, -1):
    for j in range(len(lista)):
        if num <= lista[j]:
            pos = j
    print(pos)
    lista.insert(pos, num)




print(lista)
'''
'''
lista = list()


for i in range(0, 5):
    posicao = i
    num = int(input('digite um valor: '))
    for j, pos in enumerate(lista):
        if num >= j:
            posicao = pos
    lista.insert(posicao,num)
print(lista)
'''