# verificar os tipos de um dado informado pelo usuario

var = input('Digite algo: ')
print('Foi digitado: {} cujo valor primitivo é {}'.format(var, type(var)))

print('AlfaNumerico ?',var.isalnum())
print('Alfa         ?',var.isalpha())
print('Numerico     ?',var.isnumeric())
print('Spaces       ?',var.isspace())
print('Boolean      ?',var=='True')
print('Decimal      ?',var.isdecimal())
print('Upper        ?',var.isupper())
print('Lower        ?',var.islower())

