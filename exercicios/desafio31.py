print('============ Calculando valor da Viagem =============')
km = float(input('Informe a distância da viagem em Km '))

#aplciation condition
if km <= 200:
    valor = km * 0.50
    print('O valor estipulando para essa viagem será {:.2f}R$ '.format(valor))
else:
    valor = km * 0.45
    print('O valor estipulando para a viagem acima de 200Km será {:.2f}R$ '.format(valor))