print('========= Calculando o Salário ===========')
salario = float(input('Informe o salário R$ '))

#conditions
if salario > 1250.00:
    nvsalario = salario * 0.10
    salario = salario + nvsalario
    print('O valor do reajuste com 10% será : {:.2f} R$ e o salário passa a ficar {:.2f} R$'.format(nvsalario,salario))
elif salario < 1250.00:
    nvsalario = salario * 0.15
    salario = salario + nvsalario
    print('O valor do reajuste com 15% será : {:.2f} R$ e o salário passa a ficar {:.2f} R$'.format(nvsalario,salario))