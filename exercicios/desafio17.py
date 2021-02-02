print('===================== Comprimento da Hipotenusa ===================')
oposto = float(input('Informe o cateto oposto '))
adjacente = float(input('Informe o cateto adjacente '))

#fazer importação do modulo math, o metedo hypot.
from math import hypot

hipo = hypot(oposto,adjacente)

print('A soma dos quadrados dos catatos oposto {} e adjacente {} terá como hipotenusa {:.2f} '.format(oposto,adjacente,hipo))