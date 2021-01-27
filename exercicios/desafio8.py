metro = int(input('Informe a metragem '))

cm = metro * 100
mm = metro * 1000
km = metro / 1000

print('O valor {} em metro(s) convertidos em centímetros será {:.0f}cm e em milímetros será {:.0f}mm \n '
      'em Quilomêtros será {}km '.format(metro,cm,mm,km))
