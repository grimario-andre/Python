print('========= Vamos joga Joken Po ============')
#import module random
import random
from time import sleep

jogadapc = random.randint(1,3)
jogada = ''

#condition
if jogadapc == 1:
    jogada = 'papel'
elif jogadapc == 2:
    jogada = 'pedra'
else:
    jogada = 'tesoura'

jogadap = str(input('Faça sua escolha\n Pedra\n Papel\n Tesoura ')).lower().strip()

print('1, 2, 3 e já! ')
sleep(3)

#condition for comparation
if jogada == jogadap:
    print('Deu empate, vamos novamente ')
elif jogada == 'pedra' and jogadap == 'papel':
    print('Parabéns, você ganhou, papel vence pedra. ')
elif jogada ==  'papel' and jogadap == 'tesoura':
    print('Parabéns, você ganhou, tesoura vence papel. ')
elif jogada == 'tesoura' and jogadap == 'pedra':
    print('Parabéns, você ganhou, pedra vence tesoura. ')
else:
    print('HA HA, Ganhei!')

