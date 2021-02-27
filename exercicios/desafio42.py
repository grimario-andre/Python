print('========== Verificador de Triângulos ==========')
#import module
from time import sleep

A = int(input('Valor da reta A '))
B = int(input('Valor da reta B '))
C = int(input('Valor da reta C '))

print(''' Condição de existência de um triângulo.
Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre maior que a medida do terceiro
, então, eles podem formar um triângulo \n''')

#conditions
AB = A + B
AC = A + C
CB = C + B
X = 0

print('Verificando, aguarde ...!')
sleep(3)
if AB > C:
    print('A soma entre {} e {} é maior que {}'.format(A,B,C))
    if  AC > B:
        print('a soma entre {}  e {} é maior que {} '.format(A,C,B))
        if CB > A:
            print('A soma entre {} e {} é maior que {} \nAssim formando um trinâgulo '.format(C,B,A))
        if  A == B and A != C and B != C or A == C and A != B and C != B or B == C and B != A and C != A:
            print('Assim é formado um triângulo Isósceles ')
        elif A == B and B == C and C == A:
            print('Assim é formado um triângulo Equilátero ')
        elif A != B and B != C and C != A:
            print('Assim é formado um triângulo Escaleno ')
else:
    print('Não possível formar um triagulo ')
