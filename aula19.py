pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 22}

"""
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
pessoas['sexo'] = 'M'
pessoas['idade'] = 25
"""

print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(10 * '-')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


for k, v in pessoas.items():
    print(f'{k} = {v}')



