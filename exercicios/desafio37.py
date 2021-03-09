print('========== Esvolha a Base de conversão =============')
num = int(input('Escolha um número '))
#import module time
from time import sleep
opcao = int(input('Escolha de um 1 a 3 para escolher uma base conversão '))
print('verificando...\n ')
sleep(3)
#verificando se foi escolhido de 1 a 3
if opcao >= 1 and opcao <= 3:
   if opcao == 1:
       print('A base de conversão será binária {} '.format(bin(num)[2:]))
   elif opcao == 2:
       print('A basse de conversão será octal {} '.format(oct(num)[2:]))
   elif opcao == 3:
       print('A base de conversão será hexadecimal {} '.format(hex(num)[2:]))
else:
    print('Você não escolheu um dos valores solicitados ')
