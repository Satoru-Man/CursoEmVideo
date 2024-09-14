"""
melhore o desafio 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele
pedir para mostrar os termos.
"""

print('LAÇO COM WHILE...')
primeiro = int(input('informe o primeiro termo (a1) da PA: '))
razao = int(input('informe a razao da PA: '))
termo = primeiro
cont = 1
opcao = 10
while cont <= opcao:
    while cont <= opcao:
        print('{} ==>'.format(termo), end='')
        #termo = termo + razao
        termo += razao
        cont += 1
    print('PAUSA')
    opcao = int(input('Quantos termos você quer mostrar mais? '))
    cont = 1
print('FIM')
