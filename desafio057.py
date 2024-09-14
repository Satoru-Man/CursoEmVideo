"""
faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. caso esteja errado, peça a digitação
novamente até ter o valor correto.
"""

sexo = ' '
# while sexo != 'M' and sexo != 'F':
sexo = str(input('informe seu sexo: [M\\F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    # sexo = str(input('informe o sexo da pessoa: ')).upper()
    # retira os espaços em branco com strip() e transforma a primeira letra [0] em maiuscula com upper()
    sexo = str(input('dados inválidos Por favor tente novamente: Sexo [M\\F]: ')).strip().upper()[0]

# print(f'O sexo informado é: {sexo}')
print('Sexo {} registrado com sucesso'.format(sexo))