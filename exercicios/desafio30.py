print('============ Número Par ou Ímpar ============')
numero = int(input('Digite um número '))

resto = numero % 2

#aplication condition
if resto == 0:
    print('O número digitado é Par ')
else:
    print('o número digitado é Ímpar ')