'''
crie um programa que leia nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

nota1 = nota2 = média = 0
alunos = ['nome', [nota1, nota2, média]]
notas = []
dados = []
while True:
    nome = input('Qual o nome do aluno? ')
    nota1 = float(input('digite a nota 1: '))
    nota2 = float(input('digite a nota 2:'))
    média = (nota1 + nota2) / 2
    notas = [nota1, nota2]
    dados = [nome, notas, média]
    alunos.append(dados[:])
    dados.clear()
    notas.clear()
    if input('Deseja continuar ?') not in 'Ss':
        break

for i, pos in enumerate(alunos):
    print(f'Aluno {pos[0]} tem a média {pos[2]}')
index = 0
while (index != 999):
    index = int(input('Deseja ver a nota de qual aluno ? [999] encerra.'))
    if index > len(alunos):
        print(f'Aluno fora da faixa, digite novamente.')
    else:
        print(f'A nota do aluno {alunos[index][0]} = {alunos[index][1]}')

print('fim')
