'''
desenvolva um programa que leia
seis numeros inteiros e mostre a soma
apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o.
'''
soma = 0
for c in range(1,7):
    n = int(input('Informe o nro {}: '.format(c)))
    if (n % 2) == 0:
        soma = soma + n
    else:
        print('o nro {} digitado foi ignorado!'.format(n))
print('A soma dos numeros pares eh {}'.format(soma))
