print('============ Calculando a Média ==============')
nota1 = float(input('A primeira nota '))
nota2 = float(input('A segunda nota '))

#import modelu time
from time import sleep

print('Calculando ....')
sleep(3)

media = (nota1 + nota2) / 2

#aplicar as condições
if media < 5:
    print('Reprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')