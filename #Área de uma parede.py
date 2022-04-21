#Área de uma parede com largura e altura e tinta necessária com 2m² por litro
#Qut de tinta=area/2

larg=float(input('Insira a largura:'))
altu=float(input('Insira a altura:'))

area=larg*altu
tinta=area/2

print('Sua parede tem {0}m² \nVocê precisa de {1}L de tinta para pintar a parede!'.format(area,tinta))