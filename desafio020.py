# dados os nomes de 4 alunos, mostra-los em ordem

from random import shuffle
aluno1 = 'Pedro'
aluno2 = 'Maria'
aluno3 = 'Jose'
aluno4 = 'Fulano'

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print("alunos: {} \n".format(lista))

