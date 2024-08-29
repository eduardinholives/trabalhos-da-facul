def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while ((x< min) or (x>max)):
        x = int(input(pergunta))
    return x

def fatorial(nun):
    """
    calcula fatorial
    :param nun:
    :return:
    """
    fat = 1
    if nun == 0:
        return fat
    for i in range (1,nun+1,1):
        fat *= i# fat = fat+i
    return fat

#programa principal
x = valida_int('digite um valor:', 0, 99999)
print('{}! = {}'.format(x,fatorial(x)))
