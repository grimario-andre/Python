print('================= Calculando novo Salário ===============')
sal = float(input('Digite o valor do salário R$ '))
aumento = 15

varsal = sal * aumento / 100

nvsal = varsal + sal
print('\n')
print('O salário atual é {:.2f} R$, e agora com o acréssimo de {:.2f} R$, ficará {:.2f} R$ '.format(sal,varsal,nvsal))
