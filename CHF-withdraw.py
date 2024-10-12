'''
this program shows the quantity of notes representing an amount of value to withdraw from the cashier in a store.
'''

notas0 = (1000, 500, 200, 100, 50, 20, 10)
notas1 = ('1.000CHF', '500CHF', '200CHF', '100CHF', '50CHF', '20CHF', '10CHF')
cents0 = (5, 2, 1, 0.50, 0.20, 0.10, 0.05)
cents1 = ('5chf', '2chf', '1chf', '50cts', '20cts', '10cts', '5cts')

valor = int(input('Digite um valor: '))
print(valor)

inicio = int(input('informe a nota de maior valor: '))
index = notas0.index(inicio)
notas0 = notas0[index:]
notas1 = notas1[index:]

for i, nota in enumerate(notas0):
    #print(notas0.index(inicio))
    qtde =  valor  // notas0[i]
    valor = valor % notas0[i]
    if qtde > 0:
        print(f'{qtde} note(s) of {notas1[i]}')
print('...and...')

for i, cents in enumerate(cents0):
    qtde =  valor  // cents0[i]
    valor = valor % cents0[i]
    if qtde > 0:
        print(f'{qtde} coin(s) of {cents1[i]}')

print('fim')

'''
1. o programa deverá calcular quantas notas e moedas são necessárias para determinado valor;
2. as notas deverão ser informadas pelo usuário, que terá uma lista previamente preenchida para confirmação;
3. esta lista terá notas de 2000, 1000, 500, 200, 100, 50, 20 e 10, sendo que as notas mais utilizadas por 'default'
   serão as notas abaixo de 200. Ou seja, nesta lista de confirmação de notas, o usuário irá informar se existem 
   notas acima de 200, inclusive, ou não, apenas confirmando a seleção previamente sugerida pela aplicação;
4. para cada nota que o usuário confirmar, deverá também ser informada a quantidade de notas existentes, por exemplo: 
   o usuário vai informar que existem 2 notas de 200, 1 nota de 100, 8 notas de 50, 12 notas de 20, 3 notas de 10;
5. o programa, após a digitação e confirmação das notas deverá mostrar um total, da quantidade de notas de cada valor e 
   o total somado das notas;
6. após esta confirmação do usuário das notas presentes e a quantidade de cada nota, o usuário deverá informar um valor,
que seja múltiplo da nota de menor valor, que no caso é 10. Por exemplo, valores como 1220, 540, 130, 2910 etc;
7. de posse dessas informações, o programa deverá então calcular, pela ordem das notas de maior valor:
   a) quantas notas do maior valor confirmado devem corresponder ao valor informado;
   b) quantas notas do valor restante (valor - qtde de notas de maior valor) e assim por diante;
   c) exemplo: para notas confirmadas de 1x de 200, 2x de 100, 6x 50, 12, 20 e 9x de 10 e um valor informado de 240,
      o programa vai sugerir 1x nota de 200 e 2x notas de 20;
8. o resultado desse cálculo deverá ser impresso, detalhando para o usuário as quantidades de notas necessárias de cada 
   valor que correspondam ao valor informado pelo usuário.
'''
