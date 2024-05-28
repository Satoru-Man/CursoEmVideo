# ler a largura e altura de uma parede e verificar
# quantos litros de tinta sao necessarios para pintar a parede
# considerar que para cada 1L de tinta, pintam-se 2m2 de area

largura = float(input('informe a largura da parede: '))
altura = float(input('informe a altura da parede: '))
qtdeTinta = float((largura * altura) / 2)

print('altura = {:.2f}'.format(altura))
print('largura = {:.2f}'.format(largura))
print('area a ser pintada: {:.2f}'.format(altura * largura))
print('qtde de Tinta necessaria: {:.2f} litros'.format(qtdeTinta))

