# No python toda cadeia de caracteres será mais entre aspas simples ou duplas.

#exemplo!

frase = str('curso em video python')

# frase = str('curso em video') essa frase na linguagem python é colocada em um vetor.

#Fatiamento de string.

print(frase[9])

print(frase + '\n')
print(frase[9] + '\n')
# exibe apenas um elemento selecionado.
print(frase[9:14])
print(frase[9:21])
'''
    ao selecionar dois valores, é exibido todo o conteúdo entre esses valores.
quando o valor do rage e determinado o mesmo não entra na contagem. 
'''
print(frase[:5])
print(frase[0:5])
# Esse fatiamento quando só há o final do range, ele automáticamente considera como o valor 0 o início.
print(frase[15:])
# Esse fatiamento quando só há o início do range, ele vai ler automáticamente até o ultimo valor.
print(frase[9::3])
# Esse fatiamento quando só há o início do range, ele vai ler automáticamente até o ultimo valor pulando 3 indices.

# Análise de string
print(len(frase))
# qual é o comprimento da string.
print(frase.count('o'))
# vai contar quantas vezes a letra o minuscula.
print(frase.count('o',3,13))
# vai exibido uma contagem com fatiamento, lembrar que o ultimo valor do fatiamento não é exibido.
print(frase.find('deo'))
# vai indicar quando em qual indice vai iniciar a frase digitada.
print(frase.find('android'))
# quando a frase digitada nao for encontrada, sera retornado o valor -1.
print('curso'in frase)
# vai buscar se existe a frase digitada, obs: não é uma funcionalidade mas sim um operador.

#Transformação de string
# como via de regra, não é possível alterar uma string, porém e possível altera-la atráves de métodos.

print(frase.replace('python','android'))
# vai substituir a frase digitada pela a sequencia.
print(frase.upper())
# Irá manter as letras e deixar todas restantes em maiusculas.
print(frase.lower())
# Irá manter as letras e deixar todas restantes em manisculas.
print(frase.capitalize())
#vai deixar apenas a letra do inicio da frase em maiuscula.
print(frase.title())
# vai deixar todas a palavras da frase com a letra maiuscula.
print(frase.strip())
#remove todos 'espaços inuteis da frase'.
print(frase.rstrip())
#remove todos os espaços inuteis a direita
print(frase.lstrip())
#remove todos os espaço inuteis a esquerda.

# Divisão de string
print(frase.split())
# por padrão ele divide a string pelos espaços da frase.
print(frase.split('curso'))
# ocultar a parte digitada da frase.
print('-'.join(frase))
# vai exibir a string atráves do caracter '-'.
print('''aRhiusaehriewsfiunweiufnweiufniweunfweinfwiefnwuienf
wfiweofjweoiufnwioeufnwoeufnwoenfwe
fewnfiuowenfuiwenfiwenfenif''')
# Usando aspas triplas é possível aplicar textos utlizando um unico comando print


