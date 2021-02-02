print('=================== Escolhendo O Apagador de Lousas =========================')
import random
'''
print('Aluno 01 Gustavo; Aluno 02 André; Aluno 03 Fernanda; Aluno 04 Gilda')
print('\n')
num = random.randint(1,4)

print('O aluno sortudo que irá apagar a lousa será o número {} '.format(num))
'''

n1 = str(input('Primeiro nome '))
n2 = input('Segundo nome ')
n3 = str(input('Terceiro nome '))
n4 = input('Quarto nome ')

lista = [n1, n2, n3, n4]

sorteio = random.choice(lista)

print('O nome do aluno sorteado é {} '.format(sorteio))
