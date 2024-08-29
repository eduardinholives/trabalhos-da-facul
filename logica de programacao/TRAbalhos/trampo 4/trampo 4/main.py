print('Bem-vindo ao controle de livros do Eduardo Augusto RU:4646020')

lista_livro = []
#Lista para armazenar os livros
id_global = 0
#id de cada livro

def cadastrar_livro(id):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)
    #adiociona o livro ao catalogo
    print('Livro cadastrado')
#Função de cadastro de livros

def consultar_livro():
    print('1 - Consultar todos os livros')
    print('2 - Consultar livro por id')
    print('3 - consultar livro(s) por autor')
    print('4 - Retornar')
    consultar = input("Escolha a opção desejada: ")
    if consultar == "1":
        for livro in lista_livro:
            print(livro, end='\n')
    elif consultar == "2":
        id_consulta = int(input("Digite o id do livro: "))
        for livro in lista_livro:
            if livro["id"] == id_consulta:
                print(livro)
                break
    elif consultar == "3":
        autor= input("Digite o autor do livro: ")
        for livro in lista_livro:
            if livro["autor"] == autor:
                print(livro, end='\n')
    elif consultar == "4":
        return
    else:
        print("Opção inválida")
#Função de consulta de livros

def remover_livro():
    id_remove = int(input("Digite o id do livro que deseja remover: "))
    global lista_livro
    lista_livro = [livro for livro in lista_livro if livro["id"] != id_remove]
    print("Livro removido.")
#Função de remoção de livros

#programa principal
while True:
    print('1 - Cadastrar livros')
    print('2 - Consultar livros')
    print('3 - Remover livros')
    print('4 - Encerrar o programa')
    livros = input('escolha uma opção: ')
    if livros == "1":
        cadastrar_livro(id_global)
        id_global += 1
        #soma a id global
    elif livros == "2":
        consultar_livro()
    elif livros == "3":
        remover_livro()
    elif livros == "4":
        print("Adeus.")
        break
    else:
        print("Opção inválida")



