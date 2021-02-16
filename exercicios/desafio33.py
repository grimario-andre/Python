print('============ Exibindo o maior e o menor número =============')
num1 = int(input('Primeiro número '))
num2 = int(input('Segundo número '))
num3 = int(input('Terceiro número '))

#aplication condition
if num1 > num2 and num1 > num3:
    print('{} maior número '.format(num1))
elif num2 > num3:
    print('{} maior número '.format(num2))
else:
    print('{} maior número '.format(num3))

#low number
if num1 < num2 and num1 < num3:
    print('{} menor número '.format(num1))
elif num2 < num3:
    print('{} menor número '.format(num2))
else:
    print('{} menor número '.format(num3))
