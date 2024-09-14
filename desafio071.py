'''
crie um programa que simule o funcionamento de um caixa eletrônico.
No início pergunte ao usuário qual o valor que deseja ser sacado (inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considerar notas no caixa eletrônico de 50, 20, 10 e 1.
'''

'''
saque = 0
ced50 = ced20 = ced10 = ced1 = 0
saque = int(input('Digite o valor do saque: '))
notas = [1, 10, 20, 50]
for i in notas:
    resto = saque % notas[i]
    div = int(saque / notas[i])
    print(f'São {div} notas de R$50,00')


resto = saque

resto = resto % 50
ced50 = int(resto / 50)

resto = resto % 20
ced20 = int(resto / 20)

resto = resto % 10
ced10 = int(resto / 10)

resto = resto % 1
ced1 = int(resto / 1)


print(f'Notas de 50 {ced50}, de 20 {ced20}, de 10 {ced10} e 1 {ced1}')



'''
'''
total = int(input('digite um valor inteiro: '))
for i in (50, 20, 10, 1):
    tced = 0
    while total >= i:
        total -= i
        tced += 1
    if tced != 0:
        print(f'Total de cédulas de R$ {i}: {tced}')
print('fim')
'''

'''
Explicação dos Cálculos

Vamos detalhar o cálculo das cédulas:

    Cédulas de 50:
        valor // 50: Divide o valor total por 50 para obter o número de cédulas de 50.
    Cédulas de 20:
        (valor % 50) // 20: O operador % obtém o restante da divisão por 50. Esse restante é então dividido por 20 para obter o número de cédulas de 20.
    Cédulas de 10:
        ((valor % 50) % 20) // 10: Novamente, o operador % é usado para obter o restante da divisão por 20, e esse restante é dividido por 10 para obter o número de cédulas de 10.
    Cédulas de 1:
        ((valor % 50) % 20) % 10: Finalmente, o operador % é usado para obter o restante da divisão por 10, que será o número de cédulas de 1.

Exemplo de Execução

Vamos executar o código com um exemplo prático:

    Suponha que o usuário queira sacar R$ 135.

python

valor = 135
lista1 = [135 // 50, (135 % 50) // 20, ((135 % 50) % 20) // 10, ((135 % 50) % 20) % 10]
# lista1 será [2, 1, 1, 5]

Explicação do Cálculo:

    135 // 50 é 2 (2 cédulas de 50)
    135 % 50 é 35 (resto de 135 dividido por 50)
    35 // 20 é 1 (1 cédula de 20)
    35 % 20 é 15 (resto de 35 dividido por 20)
    15 // 10 é 1 (1 cédula de 10)
    15 % 10 é 5 (resto de 15 dividido por 10, que será 5 cédulas de 1)

Portanto, a lista lista1 contém [2, 1, 1, 5].

O laço for então imprime:

bash

Total de 2 cédulas de R$50
Total de 1 cédulas de R$20
Total de 1 cédulas de R$10
Total de 5 cédulas de R$1

Conclusão

Este código é uma maneira eficiente de calcular a quantidade de cédulas necessárias para um 
determinado valor usando a divisão inteira e o operador de módulo em Python. A lista lista1 
armazena as quantidades de cada denominação, e a lista lista2 armazena as denominações correspondentes.
O laço for é usado para iterar através das listas e imprimir os resultados somente quando a quantidade 
de cédulas é maior que zero.
'''

valor = int(input('Quanto você quer sacar? R='))
lista1 = [valor // 50, (valor%50)//20, ((valor%50)%20)//10, ((valor%50)%20)%10]
lista2 = ['R$50','R$20','R$10','R$1']
for i in range(4):
    if (lista1[i] > 0):
        print('Total de {} cédulas de {}'.format(lista1[i], lista2[i]))
print('fim')
