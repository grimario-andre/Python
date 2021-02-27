print('============= Pega Cred ==============\n')
print('Faça uma avaliação e dê entrada na sua casa nova!')
#import module time
from time import sleep

vlcasa = float(input('Informe o valor da casa R$ '))
salario = float(input('Quanto é seu salário R$ '))
anos = int(input('Em quantos você vai querer pagar '))

#calcular valor para não exceder 30% do salário.
vlexcedente = salario * 0.30

#calcular o valor das parcelas.
meses = anos * 12
vlparcela = vlcasa / meses

print('Processando... \n')
sleep(3)
print('O valor da casa é {:.2f}R$ \nO salário é {:.2f}R$ \nOs 30% permitido {:.2f}R$ \nNúmero de parcelas {}\n'
      'O valor delas {:.2f}R$'.format(vlcasa,salario,vlexcedente,meses,vlparcela))

#aplicar condição.
if vlparcela > vlexcedente:
    print('Desculpe, mas o valor das parcelas é maior que 30% do seu salário. ')
else:
    print('Parabéns, você vai poder comprar sua casa própia! ')

