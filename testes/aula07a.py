#nome = input('Qual é o seu nome? ')
#print(' Prazer em te conhecer {:>20} '.format(nome))
#print(' Prazer em te conhecer {:<20} '.format(nome))
#print(' Prazer em te conhecer {:^20} '.format(nome))
#print(' Prazer em te conhcer {:=^20} '.format(nome))

n1 = int(input('um valor'))
n2 = int(input('outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# comando end='' nao permite a quebra de linha entre comandos print.
# comando /n faz a quebra de linha

print('A soma é {}, a multiplicação é {}, a divisao é {:.2f} '.format(s,m,d), end='')
print('A divisão inteira é {} e a potência é {} '.format(di,e))