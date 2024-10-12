'''
crie um programa que tenha uma tupla com varias palavras, sem acentos.
Depois disso mostre para cada palavra quais são suas vogais
'''
import random

def criar_tupla_palavras_aleatorias(numero_palavras=10):
  """Cria uma tupla com um número específico de palavras aleatórias.

  Args:
    numero_palavras: O número de palavras desejado na tupla.

  Returns:
    Uma tupla com as palavras aleatórias.
  """

  # Lista de palavras (você pode personalizar com sua própria lista)
  palavras = ["casa", "carro", "sol", "lua", "arvore", "agua", "terra", "fogo", "vento", "nuvem",
              "montanha", "rio", "lago", "cidade", "campo", "floresta", "praia", "pedra", "areia", "mar"]

  # Seleciona um número aleatório de palavras da lista
  palavras_aleatorias = random.sample(palavras, numero_palavras)

  # Converte a lista para uma tupla
  tupla_palavras = tuple(palavras_aleatorias)

  return tupla_palavras

# Exemplo de uso:
minha_tupla = criar_tupla_palavras_aleatorias()
print(minha_tupla)

# imprime as vogais de cada palavra
vogais = 'aeiouAEIOU'
for palavra in minha_tupla:
  print(f'Na palavra {palavra.upper()} temos as vogais ', end='')
  for letra in palavra:
    if letra in vogais:
      print(letra, end=' ')
  print('')

'''
  def tem_vogal(s):
    return any(char in 'aeiouAEIOU' for char in s)

# Exemplo de uso
texto = "Python"
print(tem_vogal(texto))  # Saída: True
'''