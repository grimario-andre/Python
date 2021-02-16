print('=========== Identificador de Anos Bissextos ============')
ano = int(input(' Informe o ano '))
from datetime import date
if ano == 0:
    ano = date.today().year

print('\n')
# verificar se o ano e bissexto
bissexto = ano % 4
por100 = ano % 100
por400 = ano % 400

if bissexto == 0 and por100 != 0 or por400 == 0:
    print('O ano {} é bissexto '.format(ano))

else:
    print('Ano {} não é bissexto '.format(ano))