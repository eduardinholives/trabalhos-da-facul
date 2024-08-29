km = int(input('quantos km foram percorridos?'))
dias = int(input('por quantos dias ele foi alugado'))

preco = 60*dias+0.15*km

print('km = {}. dias {}'. format(km,dias))
print('valor a ser pago: {}.'.format(preco))
