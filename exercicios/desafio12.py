print('================== Calculando preços com descontos ==============')
preco = float(input('Informe o valor do produto '))
vldesc = int(input('O valor a porcentagem do desconto % '))
print('\n')
desc = preco * vldesc / 100
nvpreco = preco - desc

print('O valor do produto {} R$, com o desconto de {:.2f}R$ o novo valor será {:.2f} R$ '.format(preco,desc,nvpreco))
