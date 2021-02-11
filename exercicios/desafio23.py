print('============== Exibindo Valores ==============')
numeral = int(input('Digite um número '))
u = numeral // 1 % 10
d = numeral // 10 % 10
c = numeral // 100 % 10
m = numeral // 1000 % 10

#Analisar e exibir o resultado.
print('Analisando o numero {} '.format(numeral))
print('Unidade: {} '.format(u) + '\n' + 'Dezena: {}'.format(d) + '\n' + 'Centena: {}'.format(c) + '\n' +
      'Milhar: {}'.format(m)  )