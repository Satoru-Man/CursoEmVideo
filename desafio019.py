# sortear entre 4 alunos um deles para ser mostrado

from random import choice

aluno1 = 'Pedro'
aluno2 = 'Maria'
aluno3 = 'Jose'
aluno4 = 'fulano'
lista = [aluno1, aluno2, aluno3, aluno4]

print('o aluno sorteado foi: {}'.format(choice(lista)))

