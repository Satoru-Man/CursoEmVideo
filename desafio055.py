'''
faça um programa que leia o peso de cinco pessoas.
No final mostre qual foi o maior e o menor peso lidos.
'''

pesoMaior = pesoMenor = 0
pessoa = {}

for c in range(0, 5):
    pessoa[c] = float(input(f"informe o peso da pessoa {c+1}: "))
    if c == 0: pesoMenor = pessoa[c]
    if pessoa[c] >= pesoMaior:
        pesoMaior = pessoa[c]
    if pessoa[c] <= pesoMenor:
        pesoMenor = pessoa[c]

print(f"{pesoMaior} eh p maior peso")
print(f"{pesoMenor} eh o menor peso")