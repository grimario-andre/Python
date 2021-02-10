print('================== Contador de Letras ===================')
nome = str(input('Informe o nome completo '))

#contador de letras 'a'.
print(nome.count('a'))

#exibir em qual posição aparece a letra pela primeira vez.
letra = nome.split()
print(letra[:].count('a'))

#exibir em qual posição aparece a letra pela ultima vez.
