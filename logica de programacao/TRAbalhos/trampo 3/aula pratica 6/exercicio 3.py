cadastro = {'nome':[] , 'sexo':[], 'ano':[] }

while True:
    terminar = input('deseja cadastrar mais uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper()  not in 'S':
        print('digite S ou N para continuar')
        continue


    nome = input('qual seu nome?')
    sexo = input('qual seu sexo [M/F]?')
    ano = int(input('qual seu ano de nascimento?'))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)