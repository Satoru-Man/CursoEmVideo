tupla = ('a', 'b', 1, 2, True)
lista = ['a', 'b', 1, 2, True]
dicionario = {'a', 'b', 1, 2, True}
conjunto = set()
conjunto =  set(['a', 'b', 1, 2, True])

print(tupla)
print(lista)
print(dicionario)
print(conjunto)

print('-' * 20)

nomes = ["Ana", "Pedro", "Maria", "João"]
idades = [25, 30, 22, 28]

pessoas = []
for i in range(len(nomes)):
  pessoa = (nomes[i], idades[i])
  pessoas.append(pessoa)

print(pessoas)
