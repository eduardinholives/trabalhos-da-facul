print('calculadora')
print('+ adicao')
print('- subtracao')
print('/ divisao')
print('* multiplicacao')
print('pressione outra tecla para sair')

while True:
    op = input('qual operacao deseja fazer?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('digite o primeiro valor'))
        y = int(input('digite o segundo valor'))

    if (op == '+'):
        res = x + y
        print('resultado:{} + {} = {}'.format(x,y,res))
        continue
    elif (op == '-'):
        res = x - y
        print('resultado:{} - {} = {}'.format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('resultado:{} / {} = {}'.format(x, y, res))
        continue
    elif (op == '*'):
        res = x * y
        print('resultado:{} * {} = {}'.format(x, y, res))
        continue
    elif(op == 's'):
        break
    else:
        print('operacao invalida')

print('encerrando o programa')