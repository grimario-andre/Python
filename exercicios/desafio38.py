print('================== Comparando valores ================')
num1 = int(input('Primeiro número '))
num2 = int(input('Segundo número '))

#import mudole time
from time import sleep

print('Comparando...  Agurade! ')
sleep(3)

print('=======================================================')
#aplicar condição aninhada.
if num1 > num2:
    print('O Primerio número é o maior {} '.format(num1))
elif num2 > num1:
    print('O segundo número é o maior {} '.format(num2))
else:
    print('O primeiro e segundo número são iguais {}, {} '.format(num1,num2))