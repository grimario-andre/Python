print('================= Verificador de Alistamento ==================')
#import module time and datetime
from time import sleep

ano = int(input('Informe o ano de nascimento '))

print('Aguarde um momento .... Verificando! ')
sleep(3)


#calculos para cada condiçõa
anoatual = 2021

idalistar = anoatual -ano # menor de idade.

#iniciar condição.
if idalistar < 18:
    print('Você não tem idade para se alistar ')
elif idalistar == 18:
    print('Parabéns, chegou o grande momento, esta na hora de se alistar ')
else:
    print('É bom correr, pois você já passou da hora de se alistar! ')
    idalistar = idalistar * 12 #transformar anos em meses.
    print('Você estrasado em {} meses '.format(idalistar))