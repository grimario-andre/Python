print('================= Aluguél de Carro =====================')
print('\n')
qtdia = int(input('Quantos dias o carro foi alugado? '))
qtkm = int(input('Quantos Quilomêtros foram rodados? '))

#Calculando o preço do aluguél.
totvl = ((qtdia * 60) + (qtkm * 0.15))

#Resposta
print('O valor do aluguél do carro será {:.2f}R$ '. format(totvl))