def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while ((x< min) or (x>max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('erro na criação do arquivo')
    else:
        print('arquivo {} foi criado com sucesso \n'.format(nomeArquivo))
def existeArquivo(nomeArquivo):
    try:
        a=open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a=open(nomeArquivo, 'rt')
    except:
        print('erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()
def cadastrarJogo(nomeArquivo, nomeJogo , nomeConsole):
    try:
        a=open(nomeArquivo, 'at')
    except:
        print('erro ao abrir arquivo')
    else:
        a.write('{};{}\n ' . format(nomeJogo, nomeConsole))
    finally:
        a.close()

#programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computaodor')
else:
    print('arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('menu')
    print('1 - cadastrar novo jogo')
    print('2 - lista novos jogos')
    print('3 - sair')

    op = valida_int('escolha a opção desejada: ' ,1 ,3)
    if op == 1:
        print('coloca o jogo ... \n')
        nomeJogo = input('nome do jogo')
        nomeConsole = input('NOME DO CONSOLE')
        cadastrarJogo(arquivo, nomeJogo, nomeConsole)
    elif op == 2:
        print('lista de jogos... \n')
        listarArquivo(arquivo)
    elif op == 3:
        print('vazando')
        break