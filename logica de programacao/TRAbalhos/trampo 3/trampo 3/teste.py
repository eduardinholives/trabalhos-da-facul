print('Bem-vindo ao petshop do Eduardo Augusto, RU:4646020')
#mensagens de boas-vindas
def servico():
    """
    Retorna o valor o serviço escolhido

    :return:
    """
    while True:
        try:
            servico = input('entre com o serviço desejado: ')
            if servico == ("dig"):
                return 1.1
            elif servico == ('ico'):
                return 1.0
            elif servico == ('ipb'):
                return 0.4
            elif servico == ('fot'):
                return 0.2
        except:
            print('escolha inválida')

def paginas():
    while True:
        try:
            paginas = int(input('digite o número de paginas: '))
            if paginas >20000:
                print('não aceitamos tantas paginas de uma vez')
                continue
            elif paginas >=2000:
                return paginas*25
            elif paginas >= 200:
                return paginas *20
            elif paginas >= 20:
                return paginas *15
            else:
                return paginas
        except:
            print('Valor de paginas nao especificado')

def extra():
    while True:
        print('1 - encardenação simples')
        print('2 - encardenação com capa dura')
        print('0 - não, obrigado')
        extra = input('deseja encardenação? ')
        if extra == '1':
            return 15
        elif extra == '2':
            return 40
        elif extra == '0':
            return 0
        else:
            print('escolha nao especificada')



def total(s,p,e,d):
    return s * (p/100) + e - (d/100)

print('DIG - digitalização')
print('ICO - impressão colorida')
print('IPB - impress preto e branco')
print('FOT - fotocópia')

s=servico()
p=paginas()
e=extra()
d=desconto(s,p)
t=total(s,p,e,d)

print('valor total a pagar é R$: {}'.format(total(s,p,e,d)))