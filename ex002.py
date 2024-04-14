nome = input('informe um nome: ')
print('o nome digitado foi: {}'.format(nome))

print('Olá, {} 1!', nome, '\n')
print(f'Olá, {nome.upper()} 2!')
print('Olá, {} 3!'.format(nome := nome.upper()))

print("My name is {0} :-{{}}".format('Fred'))

print("My name is Fred :-{}")


'''
A linha de código em Python que você forneceu é:
Python
print('Olá, {}!'.format(nome := nome.upper()))
Use o código com cuidado. Saiba mais
Essa linha de código imprime a seguinte mensagem:
Olá, [NOME EM MAIÚSCULAS]!
Ela faz isso usando a função print() para imprimir a mensagem 'Olá, {}!'. 
A variável nome é atribuída ao valor do conteúdo da variável nome convertido para maiúsculas. 
Em seguida, a variável nome é passada como argumento para a função format(). 
A função format() usa o valor da variável nome para substituir o marcador {} na mensagem 'Olá, {}!'.
Essa linha de código pode ser simplificada usando a seguinte sintaxe:
Python
print(f'Olá, {nome.upper()}!')
Use o código com cuidado. Saiba mais
Essa sintaxe usa a função f-string para imprimir a mensagem 'Olá, [NOME EM MAIÚSCULAS]!'. A função f-string permite que você inclua variáveis ​​dentro de uma string usando a notação {variável}.
'''
