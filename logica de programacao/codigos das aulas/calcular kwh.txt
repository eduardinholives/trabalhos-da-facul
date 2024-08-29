kwh = float(input('quantos kwh foram consumidos'))
tipo = input('qaul o tipo de instalcao ( r, c ou i)')

if(tipo =='r'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'c'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif (tipo == 'i'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print('instalcao invalida')

print('total a pagar:{}'.format(kwh*preco))