print('========== Esvolha a Base de conversão =============')
num = int(input('Escolha de um 1 a 3 para escolher uma base conversão '))
#import module time
from time import sleep
print('verificando...\n ')
sleep(3)

#verificando se foi escolhido de 1 a 3
if num >= 1 and num <= 3:
   if num == 1:
       print('A base de conversão será binária ')
   elif num == 2:
       print('A basse de conversão será octal')
   elif num == 3:
       print('A base de conversão será hexadecimal')
else:
    print('Você não escolheu um dos valores solicitados ')
