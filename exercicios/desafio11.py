print('========= Calculando a Area do M² ============')
alt = float(input('Informe a altura '))
larg = float(input('Agora a largura '))
print('\n')
mquad = alt * larg
ltinta = mquad / 2

print('A area quadrada será {:.2f}m² e serão necessários {:.2f}L litros de tinta para realizar a pintura. '
      .format(mquad,ltinta))
