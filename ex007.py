# leia as duas notas de um aluno, calcule e mostre a nota media

nota1 = float(input('informe a nota 1: '))
nota2 = float(input('informe a nota 2: '))
media = (nota1 + nota2) / 2
print('as notas do aluno sao: {:.1f} e {:.1f} e sua media eh {:.1f}'.format(nota1, nota2, media))
