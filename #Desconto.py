#Descontin
#Preço pós desconto de 5% (melhorar)
#(valP/100)*valO=valF

valO=int(input('Insira o valor atual:'))
valP=int(input('Insira o valor de desconto:')) 

valD=valO*(valP/100)
valF=valO-valD
print('Seu valor descontado é {}:'.format(valF))



