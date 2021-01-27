real = float(input('Informe o valor da carteira R$ '))
cotacao = float(5.47)

dolar = real / cotacao

print('Você tem {} R$ e com esse valor poderár ser comprado {:.2f} U$ dólares '.format(real, dolar))