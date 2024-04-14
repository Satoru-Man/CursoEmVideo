"""
crie um programa que leia um nome de uma cidade e diga
se ela comeca ou nao com o nome "SANTO"
"""

cidade = input('informe um nome de cidade: ')
existeSANTO = cidade.upper().strip().startswith('SANTO')
print('nome cidade comeca com "SANTO": {}'.format(existeSANTO != 0))

' ou '

cidade = cidade.upper()
print(cidade[:5] == 'SANTO')
print('nome cidade comeca com "SANTO" {}'.format(cidade[:5] == 'SANTO'))
