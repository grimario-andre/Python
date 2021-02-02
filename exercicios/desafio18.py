print('======================= Exibir Cos,Sen e Tan ======================')
angulo = int(input('Informe o valor do angulo '))

from math import cos,tan,sin,radians
rad = radians(angulo)
coss = cos(rad)
seno = sin(rad)
tang = tan(rad)

print('O angulo escolhido {}, terá os valores de cosseno {:.2f}, seno {:.2f} e tangente {:.2f} '
      .format(angulo,coss,seno,tang))