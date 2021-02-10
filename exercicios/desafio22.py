print('================== Leito de nomes ===================')
nome = str(input('Informe o nome completo '))

#Exibir nome com todas as letras maiúsculas.
print(nome.upper())

#Exibir nome com todas as letras minúsculas.
print(nome.lower())

#Exibir todas as letras sem espaços.
print(nome.count(''))

#Exibir quantas letras tem o primerio nome.
pnome = nome.split()
print(pnome[0].count(''))
