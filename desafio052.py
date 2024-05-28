'''
faca um programa que leia um numero inteiro
e diga se ele eh ou nao um nro primo.
OBS: nros primos sao aqueles que sao divididos por 1 e por ele mesmo

===============

sígnale un valor entero a a de modo tal que 2 ≤ a ≤ n - 1.
Si a n (mod n) = a (mod n), entonces “n” probablemente sea un número primo. Si esto no se cumple, entonces “n” no es primo.
Haz lo mismo con diferentes valores de a para asegurarte de que sea realmente primo.
'''

num = int(input('informe um numero: '))
print("todos os nros primos no intervalo serão mostrados em vermelho...")
for c in range(1, num+1, 1):
    if (num % c) == 0:
        print('\033[33m', end='')  # o numero {num} informado eh primo')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print("\nFIM")
