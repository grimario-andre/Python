print('================= Verificador de Alistamento ==================')
#import module time and datetime
from time import sleep
from datetime import date

sexo = str(input('Qual é seu genero [F] ou [M]')).strip().lower()

#verificar se é homem ou mulher.
if sexo == 'f':
    print('Você, mulher não a obrigação de se alistar nas forças armadas. ')
else:
    print('Você, homem tem a obrigação de se alistar nas forças armadas. ')
    ano = int(input('Informe o ano de nascimento '))

    print('Aguarde um momento .... Verificando! ')
    sleep(3)

    # calculos para cada condiçõa
    anoatual = date.today().year

    idalistar = anoatual - ano  # menor de idade.

    # iniciar condição.
    if idalistar < 18:
        print('Você não tem idade para se alistar em {} '.format(anoatual))
    elif idalistar == 18:
        print('Parabéns, chegou o grande momento, esta na hora de se alistar em {} '.format(anoatual))
    else:
        print('É bom correr, pois você já passou da hora de se alistar! em {} '.format(anoatual))
        idalistar = idalistar * 12  # transformar anos em meses.
        print('Você estrasado em {} meses '.format(idalistar))
