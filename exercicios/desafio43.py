print('============ Calcular seu IMC ============')
#import mudole
from time import sleep

peso = float(input('Informe seu peso '))
altura = float(input('Agora sua altura '))

imc = peso / (pow(altura,2))

print('Calculando o IMC, aguarde .... ')
sleep(3)

print('Seu IMC tem o valor: {:.2f} '.format(imc))

#aplicar condições
if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Você esta no Peso ideal')
elif imc > 25 and imc < 30:
    print('Você esta com Sobrepeso')
elif imc > 30 and imc < 40:
    print('Você esta com Obesidade Severa')
else:
    print('Você esta com Obesidade Mórbida')
