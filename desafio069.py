'''
crie um programa que leia a idade e o sexo de varias pessoas.
A cada pessoa lida o programa deverá perguntar se o usuário deseja continuar ou não.
no final mostre:
a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastraaos
c) quantas mulheres tem menos de 20 anos

'''

homens = mulheres = maiores18 = mulheresmenos20 = total = 0

while True:
    sexo = input('Informe o sexo da pessoa [M ou F]: ')
    idade = int(input('Informe a idade da pessoa: '))
    sexo = sexo.strip().upper()[0]
    total += 1
    if idade > 18:
        maiores18 += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        mulheres += 1
        if idade < 20:
            mulheresmenos20 += 1
    else:
        print('por favor informe corretamente o sexo.')
    continua = input('Deseja continuar [S ou N] ? ')
    if continua in 'Nn':
        break
print('Esse é o resultado:')
print(f'Total de pessoas: {total}')
print(f'Total homens: {homens} e mulheres {mulheres}')
print(f'Homens maiores de 18 anos: {maiores18}')
print(f'Mulheres menores de 20 anos: {mulheresmenos20}')

"""
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexQ = str(input('Sexg: [M/F] ')).strip().upper() [0]
        if idade >= 18:
            tot18 += 1
        if sexo = 'M':
            totH += 1
        if sexo = 'F' and idade < 20:
            totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
        if resp = 'N':
            break
print(f'Total de pessgas com mais de 18 anos: {tot18)')
print(f'Ao todo temos {totH} homens cadastrados') print(f'E temos (totM20) mulheres com menos de 20 anos')
"""