"""
Use o código com cuidado.

Explicação do código:

    Importações:
        A biblioteca os é importada para fornecer funções para trabalhar com o sistema operacional, como renomear arquivos.
    Função renomear_arquivos:
        Essa função recebe como argumento o caminho para a pasta que contém os arquivos que você deseja renomear.
        Dentro da função:
            Um loop for itera sobre cada arquivo na pasta.
            A condição if verifica se o nome do arquivo começa com "ex" e termina com ".py". Se verdadeiro, significa que o arquivo é um candidato para renomeação.
            O número sequencial NNN é extraído do nome do arquivo usando fatiamento de string.
            O novo nome do arquivo é construído usando a string "desafio" e o número NNN extraído.
            A função os.rename() é usada para renomear o arquivo do nome antigo para o novo nome.
    Chamada da função:
        A pasta que contém os arquivos é definida na variável pasta.
        A função renomear_arquivos() é chamada com a pasta especificada como argumento.

Observações:

    Certifique-se de substituir "caminho/para/a/pasta" com o caminho real para a pasta que contém os arquivos que você deseja renomear.
    Este programa irá renomear todos os arquivos na pasta especificada que correspondem ao padrão de nome "exNNN.py".
    Se você deseja renomear arquivos em subpastas, você precisará modificar o loop for para iterar recursivamente sobre todas as subpastas.
    Este programa não verifica se o novo nome do arquivo já existe. Se um arquivo com o mesmo nome já existir, o programa irá sobrescrevê-lo.
"""

import os

"""
  Função que renomeia arquivos na pasta especificada.

  Argumentos:
    pasta (str): Caminho para a pasta que contém os arquivos.
"""
"""
# Pasta que contém os arquivos.
# pasta = "caminho/para/a/pasta"
pasta = "C:/Users/claud/PycharmProjects/CursoEmVideo/"

# Chama a função para renomear os arquivos na pasta especificada.
# renomear_arquivos(pasta)

# def renomear_arquivos(pasta):
for arquivo in os.listdir(pasta):
    if arquivo.startswith("ex") and arquivo.endswith(".py"):
        # Extrai o número NNN do nome do arquivo.
        numero = arquivo[2:-3]

        # Constrói o novo nome do arquivo.
        novo_nome = f"desafio{numero}.py"

        # Renomeia o arquivo.
        # os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))
        print('nome anterior {} ==> nome novo {}'.format(arquivo, novo_nome))

"""

import os
import re

# Diretório onde estão os arquivos
diretorio = 'C:/Users/claud/PycharmProjects/CursoEmVideo/'

# Expressão regular para encontrar arquivos que seguem o padrão 'exNNN.py'
padrao_arquivo = re.compile(r'^ex(\d{3})\.py$')

# Percorrer todos os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    # Verificar se o arquivo corresponde ao padrão
    match = padrao_arquivo.match(nome_arquivo)
    if match:
        # Extrair o número NNN
        numero = match.group(1)
        # Criar o novo nome de arquivo
        novo_nome = f'desafio{numero}.py'
        # Caminho completo dos arquivos
        caminho_antigo = os.path.join(diretorio, nome_arquivo)
        caminho_novo = os.path.join(diretorio, novo_nome)
        # Renomear o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f'Renomeado: {nome_arquivo} -> {novo_nome}')