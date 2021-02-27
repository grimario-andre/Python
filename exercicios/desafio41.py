print('========= Define Categoria ============')

anonasci = int(input('Informe o ano de nascimento '))

#import module time
from time import sleep

print('Aguarde um monento ... ')
sleep(3)

anoatual = 2021;

idade =  anoatual - anonasci

#aplicar condições
if idade <= 9:
    print('Categoria Mirin')
elif idade > 9 and idade <= 14:
    print('Categoria Infantil')
elif idade >14 and idade <= 19:
    print('Categoria Junior')
elif idade > 19 and idade <= 20:
    print('Categoria Sênior')
else:
    print('Categoria Master')