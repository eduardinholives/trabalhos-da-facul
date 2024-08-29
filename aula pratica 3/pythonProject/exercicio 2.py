valor = int(input('digite o valor em reais'))

while True:
    if valor >= 100:
        cedulas100 = valor // 100
        valor = valor - cedulas100 * 100
        print('cedulas de 100: {}'.format(cedulas100))
        if not valor:
            break
    if valor >= 50:
        cedulas50 = valor // 50
        valor = valor - cedulas50 * 50
        print('cedulas de 50: {}'.format(cedulas50))
        if not valor:
            break
    if valor >= 20:
        cedulas20 = valor // 20
        valor = valor - cedulas20 * 20
        print('cedulas de 20: {}'.format(cedulas20))
        if not valor:
            break
    if valor >= 10:
        cedulas10 = valor // 10
        valor = valor - cedulas100 * 10
        print('cedulas de 10: {}'.format(cedulas10))
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor // 5
        valor = valor - cedulas5 * 5
        print('cedulas de 5: {}'.format(cedulas5))
        if not valor:
            break
    if valor:
        cedulas1 = valor
        print('cedulas de 1: {}'.format(cedulas1))
        break