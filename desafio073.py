'''
crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato brasileiro de futebola, na ordem de colocação.
Depois mostre:
A) apenas os 5 primeiros colocados
B) os últimos 4 colocados
C) uma lista com os times em ordem alfabética
D) em que posição na tabela está o time da Chapecoense
'''

'''
3 formas de usar o loop no for
lanche = ('hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'eu vou comer {comida}')
    
for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posicao {cont}')
    
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posicao {pos}')
'''

brasileirao_2023 = (
    "Botafogo",
    "Palmeiras",
    "Grêmio",
    "Flamengo",
    "Fluminense",
    "Athletico-PR",
    "Atlético-MG",
    "Fortaleza",
    "Bragantino",
    "São Paulo",
    "Internacional",
    "Cuiabá",
    "Cruzeiro",
    "Corinthians",
    "Santos",
    "Bahia",
    "Vasco da Gama",
    "Goiás",
    "América-MG",
    "Coritiba"
)
print('A) os 5 primeiro colocados no campeonato são: ')
for i in range(5):
    print(f'{i+1:2} - {brasileirao_2023[i]}')
print('')

print('B) os últimos 4 colocados são:')
for i in brasileirao_2023[::-1]:
    if brasileirao_2023.index(i) > 15:
        print(f'{brasileirao_2023.index(i) + 1} - {i}')
print('')

print('C) os times em ordem alfabética são: ')
sorteado = sorted(brasileirao_2023)
for pos, i in enumerate(sorteado):
    print(f'{pos} - {i}')
print('')

print(f'D) o time São Paulo está na posição {brasileirao_2023.index('São Paulo')+1}')
