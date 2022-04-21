#Metros para mm e cm

metros=int(input('Insira o valor em metros: '))
cent=metros*100
mili=metros*1000
km=metros/1000

print('{0}m tem {1}cm! \n{0}m tem {2}mm! \n{0}m são {3}km!'.format(metros,cent,mili,km))