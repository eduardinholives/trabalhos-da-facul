preco = float(input('digite o preço do seu produto'))
p = float(input('digite o percentual de desconto(0-100)%:'))

desconto = preco *(p/100)
final = preco - desconto

print('o preço do produto é {}. desconto de {}%'.format(preco,desconto))
print('o valor calculado de desconto: {}. o valor final do produto:  {}'.format(desconto,final))