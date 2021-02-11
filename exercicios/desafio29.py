print('======== Radar Móvel ========')
#Import random module
from random import randint
limit = randint(80,120)
print('A velocidade marcada foi {} '.format(limit))

#to aplication condition
if limit > 80:
    ultrapassado = limit - 80
    multa = ultrapassado * 7
    print('Foram ultrapassados {}km, o valor da multa a ser paga será {:.2f}R$ '
          .format(ultrapassado,multa))
