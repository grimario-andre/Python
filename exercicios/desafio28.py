print('======= Descubra o número ======')
#import module
from random import randint

#atribute random number in a varible
n = randint(0,5)

num = int(input('Digite um número de 0 a 5 '))

#Condition for valedate choose user.
if not num < 0 >  5:
    print(' Número digitado maior ou menor que solicitado {}'.format(num))
elif num == n:
    print('Parabéns, você acertou o número {} '.format(n))
else:
    print('Ah, não foi dessa dessa vez, número sorteado {} número digitado {} '.format(n,num))

