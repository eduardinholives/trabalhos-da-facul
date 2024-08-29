print('Bem-vindo a loja do Eduardo Augusto RU:4646020')
#Mensagen de boas-vindas
print('-'*20, 'cardápio', '-' *20)
print('-'*6, '|', 'Tamanho', '|', "Cupuaçu(CP)", '|', 'Açai(AC)', '|', '-'*6)
print('-'*6, '|', "  ", 'P', '  ', "|", 'R$ 10,00', '  ','|','R$ 15,00', '|', '-'*6 )
print('-'*6, '|', "  ", 'M', '  ', "|", 'R$ 15,00', '  ','|','R$ 17,00', '|', '-'*6 )
print('-'*6, '|', "  ", 'G', '  ', "|", 'R$ 19,00', '  ','|','R$ 21,00', '|', '-'*6 )
print('-'*50)
#desgin do menu

valor = 0
#valor para a soma do preço ao ser pago no final

while True:
    op = input('Entre com o sabor desejado? (CP/AC)')
    if (op == "cp" or op == "ac"):
        tm = input('Qual o tamanho desejado? (P,M,G)')
        if (tm == "p" or tm == "m" or tm == "g"):
            #inputs de sabor e tamanho
            if op == "cp":
                if tm == "p":
                    preco = 9
                elif tm == 'm':
                    preco = 14
                elif tm == 'g':
                    preco = 18
            elif op == "ac":
                if tm == "p":
                    preco = 11
                elif tm == 'm':
                    preco = 16
                elif tm == 'g':
                    preco = 20
            valor += preco
            #Formúla para calcular o valor gasto
            combo = input('deseja pedir mais alguma coisa? (S/N)')
            if (combo == "s"):
                continue
            elif (combo == "n"):
                break
            #encerra o looping
        elif print('Tamanho invalído. tente novamente'):
            continue
    elif print('Sabor invalído. tente novamente'):
        continue
    #Mensagens de erro quando a informação for colocada errada

print('valor total a ser pago: R${}'.format(valor))
#mensagem com o valor final