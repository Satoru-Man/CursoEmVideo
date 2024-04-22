"""
leia duas notas de um aluno e calcule
sua media, mostrando uma mensagem no final de acordo com a
media atingida

- media abaixo de 5.0: reprovado
- media entre 5.0 e 6.9: recuperação
- media 7.0 ou superior: aprovado
"""

n1 = float(input('informe a nota 1: '))
n2 = float(input('informe a nota 2: '))
media = (n1 + n2) / 2
print('tirando as notas {:.1f} e {:.1f} sua media eh: {}' .format(n1, n2, media))

print('sua media foi de {:.2f}'.format(media))

if media >= 7.0:
    print('aluno aprovado')
elif media > 5.0 and media < 6.9:
    print('aluno em recuperacao')
else:
    print('aluno reprovado')

