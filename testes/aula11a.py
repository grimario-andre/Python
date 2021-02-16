print('========== Cores em Python ===========')

#padrão ANSI que melhor funciona no Python

print('\033[1;31;43mOlá Mundo!\033[m')
print('\033[0;35;46mOlá Mundo!\033[m')
print('\033[4;33;41mOlá Mundo!\033[m')
print('\033[7;37;46mOlá Mundo!\033[m')

#formatando variaveis
a = 3
b = 5
print('Os valore são \033[32m{} e \033[31m{}'.format(a,b))

#formatação avançada
nome = 'GUANABARA'
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[36m'))