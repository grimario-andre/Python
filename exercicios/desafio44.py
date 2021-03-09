print('=========== Condições de Pagamento =============')
#import module
from time import sleep

preco = float(input('Digite o preço do produto R$ '))
condicao = str(input('Agora a forma de pagamento \n Dinheiro ou Cheque \n debito \n 2x no cartao \n 3x ou mais no '
                     'cartao '
                     '').strip(

).lower())

print('Calculando novo preço com base na forma de pagamento, aguarde.... ')
sleep(3)

#aplicar condições
if condicao == 'dinheiro' or condicao == 'cheque':
    juros = preco * 0.10
    nvpreco = preco - juros
    print('O valor para pagamento a vista terá 10% de desconto asism o fica vai para: {:.2f}R$ '.format(nvpreco))
elif condicao == 'debito':
    juros = preco * 0.05
    nvpreco = preco - juros
    print('O valor para pagamento a vista com cartão terá 5% de desconto asism o fica vai para: {:.2f}R$ '.format(
        nvpreco))
elif condicao == '2x no cartao':
    print('O valor para pagamento em 2x no cartão não terá descontos {:.2f}R$ '.format(preco))
else:
    juros = preco * 0.20
    nvpreco = preco + juros
    print('O valor para pagamento em 3x ou mais no cartão terá juros de 20%, {:.2f}R$ \n assim o preco vai para {'
          ':.2f}R$ '
          ''.format(juros,nvpreco))
