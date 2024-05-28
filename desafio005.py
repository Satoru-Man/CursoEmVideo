"""
     + adicao
     - subtracao
     * multiplicacao
     / divisao
     ** potencia  pow(arg1, arg2)
     // inteiro da divisao
     %  resto da divisao


     ordem de precedencia da operacao aritmetica
     1 - ()        (o que estiver dentro de parenteses)
     2 - **        (exponenciacao)
     3 - * /  // % (multiplicacao e/ou divisao e/ou inteiro divisao e/ou resto divisao)
     4 - + -       (soma e/ou subtracao)

     ex:
     5 + 3 * 2 = 11
     3 * 5 + 4 ** 2 = 31
     3 * (5+4) ** 2 = 243
"""

''' 
OBS: 'oi'*4 = 'oioioioi'   '='*10 => '=========='
'''
n1 = float(input('Informe um valor n1: '))
n2 = float(input('Informe um valor n2: '))
s = n1 + n2
d = n1 / n2
exp = n1 ** n2
ntr = n1 // n2
res = n1 % n2

print('valor da soma {:.4f} \n '
      'valor da divisao {:.4f} \n '
      'valor da exponenciacao {:.4f}'.format(s,d,exp), end=' >>>> \n')
print ('inteiro da divisão: {} \n resto da divisao: {}'.format(ntr, res))


# crie um programa que, dado um nro inteiro, mostre seu antecessor e seu sucessor
num = int(input('Informe um nro: '))
print('O nro digitado foi {}, seu antecessor: {}, seu sucessor: {}'.format(num,num-1,num+1))
