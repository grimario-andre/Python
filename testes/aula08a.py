#Para chamar todas as funcionalidades dos moódulos/biblioteca basta usar o comando import(modulo).
#Para chamar um metédo de um módulo/biblioteca basta usar o comando 'from(modulo)import(método).

#Funcionalidades da biblioteca Math:
#ceil;floor;trunc;pow;sqrt;factorial;

#exemplo: import(Math)
#exemplo: from(Math)import(sqrt)
#exemplo: from(Math)import(sqrt,ceil)

#import math
from math import sqrt,floor
num =int(input('Digite um número '))

#raiz = math.sqrt(num)
raiz = sqrt(num)

#print('O número {} tem a seguinte raiz {} '.format(num, math.floor(raiz)))
print('O número {} tem a seguinte raiz {} '.format(num, floor(raiz)))

