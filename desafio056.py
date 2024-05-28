'''
desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final mostre:
- a media de idade do grupo
- qual o nome do homem mais velho
- quantas mulheres tem menos de 20 anos
'''

dados = [
    {'nome': '', 'idade': 0, 'sexo': ''},
    {'nome': '', 'idade': 0, 'sexo': ''},
    {'nome': '', 'idade': 0, 'sexo': ''},
    {'nome': '', 'idade': 0, 'sexo': ''}
]
mediaIdadeGrupo = 0
idadeHomemMaisVelho = 0
nomeHomemMaisVelho = ''
qtdeMulheresMenos20 = 0
for c in range(0, 4):
    pessoa = dados[c]
    pessoa['nome'] = input(f"informe o nome da pessoa {c+1}: ")
    pessoa['idade'] = int(input(f"informe a idade da pessoa {c + 1}: "))
    pessoa['sexo'] = input(f"informe o sexo da pessoa {c + 1}: ")
    print("*"*10)
    mediaIdadeGrupo = mediaIdadeGrupo + pessoa["idade"]

    if pessoa['sexo'] == 'M':
        if pessoa['idade'] >= idadeHomemMaisVelho:
            idadeHomemMaisVelho = pessoa['idade']
            nomeHomemMaisVelho = pessoa['nome']
    else:
        if pessoa['idade'] < 20:
            qtdeMulheresMenos20 = qtdeMulheresMenos20 + 1

mediaIdadeGrupo = mediaIdadeGrupo / 4
print("Das 4 pessoas informadas:")
print(f"a media de idade do grupo eh de {mediaIdadeGrupo:2} anos")
print(f"o nome do homem mais velho eh {nomeHomemMaisVelho}")
print(f" E {qtdeMulheresMenos20} mulheres tem menos de 20 anos")
