print('================= Calculando novo Salário ===============')
sal = float(input('Digite o valor do salário '))
desc = 15

varsal = sal * desc / 100

nvsal = varsal + sal

print('O salário atual é {:.2f} R$, e agora com o acréssimo de {:.2f} R$, ficará {:.2f} R$ '.format(sal,varsal,nvsal))
