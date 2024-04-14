"""
desenvolva uma logica que leia o peso e a altura de uma pessoa
calcule seu IMC e mostre o status de acordo com a tabela abaixo:
- menor ou igual a 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- entre 25 e 30_ sobrepeso
- acima de 40: obesidade morbida
"""
peso = float(input('informe o peso: '))
altura = float(input('informe a altura: '))
imc = peso / (altura ** 2)
print('o IMC calculado eh de {:.2f}'.format(imc))
if imc <= 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25.1:
    print('peso ideal')
elif imc >= 25 and imc < 30.1:
    print('sobrepeso')
elif imc >= 30 and imc < 40.1:
    print('obeso')
else:
    print('obesidade morbida')
