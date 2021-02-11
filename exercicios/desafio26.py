print('================== Contador de Letras ===================')
nome = str(input('Informe o nome completo ')).strip().upper()

#contador de letras 'a'.
print('A letra aparece tantas {} vezes na fraze '.format(nome.count('A')))

#exibir em qual posição aparece a letra pela primeira vez.
#print(letra[:].count('a'))
print('A primeira letra A foi encontrada na posição {} '.format(nome.find('A') + 1))

#exibir em qual posição aparece a letra pela ultima vez.
print('A ultima letra A foi encontrada na posição {} '.format(nome.rfind('A')))