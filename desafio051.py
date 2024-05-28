'''
desenvolva um programa que leia o primeiro termo
e a razao de uma PA.
No final mostre os 10 primeiros termos
dessa progressao.
'''
'''
Elementos de uma progressão aritmética (PA):
Uma progressão aritmética (PA) é uma sequência de números em que a diferença entre dois termos consecutivos é sempre a mesma. Essa diferença constante é chamada de razão da PA.
Elementos de uma PA:
    Termo geral: É a fórmula que define qualquer termo da PA. Ela permite calcular o valor de qualquer termo da sequência sem precisar conhecer todos os termos anteriores. A fórmula do termo geral de uma PA é:
an = a1 + r(n - 1)
Onde:
    an: é o n-ésimo termo da PA;
    a1: é o primeiro termo da PA;
    r: é a razão da PA;
    n: é a posição do termo na sequência (n-ésimo termo).
    Termos adjacentes: São dois termos consecutivos da PA. A diferença entre dois termos adjacentes é sempre a razão da PA.
    Termos equidistantes: São termos da PA que estão a mesma distância uns dos outros. A diferença entre dois termos equidistantes é sempre um múltiplo da razão da PA.
    Termos extremos: São o primeiro e o último termo da PA. A diferença entre os termos extremos é igual à razão multiplicada pelo número de termos da PA menos 1.
Exemplo:
Considere a seguinte PA: 3, 6, 9, 12, 15, ...
    Primeiro termo (a1): 3
    Razão (r): 3 (a diferença entre os termos consecutivos é sempre 3)
    Termo geral: an = 3 + 3(n - 1)
    Termos adjacentes: 3 e 6, 6 e 9, 9 e 12, ...
    Termos equidistantes: 3 e 12 (a distância entre eles é 9, que é 3 * 3), 6 e 15 (a distância entre eles é 9, que é 3 * 3), ...
    Termos extremos: 3 (primeiro termo) e 15 (último termo). A diferença entre os termos extremos (15 - 3) é igual à razão (3) multiplicada pelo número de termos da PA (6) menos 1 (5).
Propriedades das PAs:
    Propriedade dos termos equidistantes: A soma de dois termos equidistantes de uma PA é igual à soma dos termos extremos.
    Propriedade da média aritmética: O termo médio de uma PA é igual à média aritmética dos seus termos extremos.
    Propriedade da soma dos termos: A soma dos termos de uma PA finita é igual ao produto da média aritmética dos seus termos extremos pelo número de termos da PA.
Aplicações das PAs:
As PAs são utilizadas em diversas áreas, como matemática, física, engenharia, finanças e até mesmo em jogos e puzzles.
Recursos adicionais:
    https://www.youtube.com/watch?v=ej0TS0rNLHg
    https://www.todamateria.com.br/progressao-aritmetica/
    https://pt.khanacademy.org/math/algebra/x2f8bb11595b61c86:sequences/x2f8bb11595b61c86:introduction-to-arithmetic-sequences/a/introduction-to-arithmetic-sequences
'''
print('''Sendo uma PA ==> an = a1 + r(n - 1)
      an = a1 + r(n - 1)
Onde:
    an: é o n-ésimo termo da PA;
    a1: é o primeiro termo da PA;
    r: é a razão da PA;
    n: é a posição do termo na sequência (n-ésimo termo).''')

print()
a1 = int(input('informe o primeiro termo (a1) da PA: '))
r = int(input('informe a razao da PA: '))
an = a1 + (10 - 1) * r

print('Esta e uma PA de termo {} e razao {}'.format(a1, r))
print(f'Esta e uma PA de termo {a1} e razao {r}')

c = a1 - a1
for c in range(a1, an + r, r):
    print(c, end='-> ')
print("FIM")
