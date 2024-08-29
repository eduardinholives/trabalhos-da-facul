a=int(input('digite o primeiro lado do triangulo'))
b=int(input('digite o segundo lado do triangulo'))
c=int(input('digite o terceiro lado do triangulo'))

if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a :
#se chegou ate aqui o triangulo e valido
        if a!=b and a!=c and b!=c:
            print('escaleno')
        else:
            if a==b and a==c and b==c:
                print('equilatero')
            else:
                print('isoceles')
    else:
        print('nao e um triangulo')
else:
    print('nao e um triangulo')