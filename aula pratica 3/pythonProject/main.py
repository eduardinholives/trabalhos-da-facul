print('calculadora')
print('+ adicao')
print('- subtracao')
print('/ divisao')
print('* multiplicacao')
print('pressione outra tecla para sair')


op = input('qual operacao deseja fazer?')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('digite o primeiro valor'))
    y = int(input('digite o segundo valor'))

while(op != "s"):
    if (op == '+'):
        res = x + y
        print('resultado:{} + {} = {}'.format(x,y,res))
    elif (op == '-'):
        res = x - y
        print('resultado:{} - {} = {}'.format(x, y, res))
    elif (op == '/'):
        res = x / y
        print('resultado:{} / {} = {}'.format(x, y, res))
    elif (op == '*'):
        res = x * y
        print('resultado:{} * {} = {}'.format(x, y, res))
    else:
        print('operacao invalida')

    op = input('qual operacao deseja fazer?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('digite o primeiro valor'))
        y = int(input('digite o segundo valor'))

print('encerrando o programa')