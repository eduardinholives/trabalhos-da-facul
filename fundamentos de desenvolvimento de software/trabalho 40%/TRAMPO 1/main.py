print('Bem-vindo a loja do Eduardo Augusto, RU:4646020')
#mensagem de boas-vindas
valor = float(input('valor unitário do produto'))
quantidade = int(input('quantidades de produtos'))
#inputs para o usuario preencher
total = valor * quantidade
#formúla para calcular o valor sem desconto
if total < 2500:
    p = 0
elif total >=2500 and total < 6000:
    p = 4
elif total >= 6000 and total < 10000:
    p=7
else:
    p=11
#variáveis para calcular o desconto
desconto = total * p / 100
final = total - desconto
#formúla para calcular o valor com desconto
print('o valor total do produto foi {}'.format(total))
print('o valor com desconto foi {}'.format(final))
#mensagens informando os valores
