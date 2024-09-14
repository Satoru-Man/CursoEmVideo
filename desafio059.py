"""
crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior nro
[4] novos números
[5] sair do programa

o programa deverá realizar a operação em cada caso
"""

opcao = 0
while opcao != 5:
    try:
        print('Informe dois números e diga qual opção deseja:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        print('-='*20)
        print('[ 1 ] Somar\n'
              '[ 2 ] Multiplicar\n'
              '[ 3 ] Qual é o maior nro\n'
              '[ 4 ] Novos números\n'
              '[ 5 ] Sair do programa')
        opcao = int(input('Qual é sua opção? '))
        if opcao == 1:
            print('A soma dos dois números é: {}'.format(num1 + num2))
        elif opcao == 2:
            print('A multiplicação dos dois números é: {}'.format(num1 * num2))
        elif opcao == 3:
            if num1 > num2:
                print('O maior número é o primeiro informado: {}'.format(num1))
            elif num1 < num2:
                print('O maior número é o segundo informado: {}'.format(num2))
            else:
                print(f'Os números informados {num1} e {num2} são iguais.')
        elif opcao == 4:
            print('novos números...')
        elif opcao ==5:
            print('Saindo do programa.')
        else:
            print('Opção inválida.')
    except Exception as e:
        print(f'Erro. Informe valores válidos. ==> {e}')
print('Fim.')