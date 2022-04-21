#Soma e média 
#Input de nota1 e 2: (nota1+nota2)/2=MEDIA

vNota1=int(input('Insira nota 1: '))
vNota2=int(input('Insira nota 2: '))
vSoma=(vNota1+vNota2)/2

print('A média do aluno com a nota 1: {1} \nE nota 2: {0:>23}\n É igual a {2}!'.format(vNota2,vNota1,vSoma))
