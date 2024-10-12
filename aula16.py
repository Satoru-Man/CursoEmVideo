num = list()  # ou num = []

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.append(4)
num.pop(2)  # sem index, elimina o último: num.pop()
if 4 in num:
    print(f'foi encontrado o numeral 4, que será excluído (tamanho: {len(num)})')
    num.remove(4)
    print(f'excluído o numeral (tamanho: {len(num)})')
else:
    print('não achei o numeral 4 na lista')
print(num)
print(f'esta lista tem {len(num)} elementos')
