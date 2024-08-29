print('Bem-vindo ao petshop do Eduardo Augusto, RU:4646020')
#mensagens de boas-vindas
def servico():
    """
    Retorna o valor do serviço escolhido
    """
    while True:
        servico = input('entre com o serviço desejado: ')
        if servico == ("dig"):
            return 1.1
        elif servico == ('ico'):
            return 1.0
        elif servico == ('ipb'):
            return 0.4
        elif servico == ('fot'):
            return 0.2
        else:
            print('escolha inválida')
#Função para escolher o serviço

def paginas():
    """
    Retorna o número de páginas e o desconto referente a elas ate 20000 páginas

    """
    while True:
        try:
            paginas = int(input('digite o número de paginas: '))
            if paginas >20000:
                print('não aceitamos tantas páginas de uma vez')
                continue
            elif paginas >=2000:
                return paginas*0.75
            elif paginas >= 200:
                return paginas * 0.80
            elif paginas >= 20:
                return paginas * 0.85
            else:
                return paginas
        except:
            print('Valor de páginas nao especificado')
#Função para escolher o numero de páginas

def extra():
    """
    Retorna a escolha do usuario pelo tipo de capa do serviço
    1=15(capa simples)
    2=40(capa dura)
    0=0 (sem capa)
    """
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
#Função para adicionar o extra

def total(s,p, e):
    '''
    Retorna formula para calcular o valor total que o usuario ira pagar
    :param s: modelo de impressão
    :param p: número de paginas
    :param e: modelo de capa
    :return:s*p+e
    '''
    return s * p + e
#Função que calcula o total

#codigo principal(main)
print('DIG - digitalização')
print('ICO - impressão colorida')
print('IPB - impress preto e branco')
print('FOT - fotocópia')
#opções de impressão para o usuario
s=servico()
p=paginas()
e=extra()
t=total(s,p,e)

print('valor total a pagar é R$: {}'.format(total(s,p,e)))
#valor final a ser pago ja calculado



