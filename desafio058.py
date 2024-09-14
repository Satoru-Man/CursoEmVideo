"""
melhore o jogo do desafio 028
onde o computador vai 'pensar' em um numero
entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar o número, mostrando ao final quantos palpites
foram necessários para vencer.
"""

from random import randint

numComp = randint(0,10)
nroVezes = 0
acertou = False
while not acertou:
    try:
        numUsr = int(input('Informe nro que o computador pensou: '))
        nroVezes += 1
        if numUsr != numComp:
            if numUsr < numComp:
                print('Mais...Tente mais uma vez!')
            elif numUsr > numComp:
                print('Menos...Tente mais uma vez!')
            # else:
                # print("Não é esse o nro, tente novamente!")
        else:
            acertou = True
            print(f"Você tentou {nroVezes} vezes até acertar o número {numComp}")
    except Exception as e:
        print(f"Erro. Digite um valor válido ==> {e}")
