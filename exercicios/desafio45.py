print('========= Vamos joga Joken Po ============')
#import module random
import random
from time import sleep
jogada = random.randint(1,3)
jogadapc = ''
#condition
if jogada == 1:
    jogadapc = 'papel'
elif jogada == 2:
    jogadapc = 'pedra'
else:
    jogadapc = 'tesoura'
jogadap = str(input('Faça sua escolha\n Pedra\n Papel\n Tesoura \n')).lower().strip()
print('JO KEN PO! ')
sleep(2)
#condition for comparation
if jogadapc == jogadap:
    print('Deu empate, vamos novamente ')
elif jogadapc == 'pedra' and jogadap == 'papel':
    print('Parabéns humano, papel vence pedra. ')
elif jogadapc ==  'papel' and jogadap == 'tesoura':
    print('Parabéns humano, tesoura vence papel. ')
elif jogadapc == 'tesoura' and jogadap == 'pedra':
    print('Parabéns humano, pedra vence tesoura. ')
else:
    print('HA HA, IA WINS ;)')
