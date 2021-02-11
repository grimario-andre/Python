print('================== Leito de nomes ===================')
nome = str(input('Informe o nome completo ')).strip()

#Exibir nome com todas as letras maiúsculas.
print('Seu nome em maiúsculas é: {} '.format(nome.upper()))

#Exibir nome com todas as letras minúsculas.
print('Seu nome em minúsculas é: {} '.format(nome.lower()))

#Exibir todas as letras sem espaços.
print(len(nome) - nome.count(' '))

#Quantas letras tem o primeiro nome.
separa =  nome.split()
#print(separa[0].find(''))
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0],len(separa[0])))