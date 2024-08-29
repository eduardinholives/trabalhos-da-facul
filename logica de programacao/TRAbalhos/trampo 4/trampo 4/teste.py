# [EXIGÊNCIA DE CÓDIGO 1 de 8]
# Mensagem de boas-vindas com o nome do desenvolvedor
print("Bem-vindo ao Sistema de Gerenciamento de Livros! Desenvolvido por Seu Nome.")

# [EXIGÊNCIA DE CÓDIGO 2 de 8]
# Lista vazia para armazenar os livros e variável id_global para controlar os IDs
lista_livro = []
id_global = 0

# [EXIGÊNCIA DE CÓDIGO 3 de 8]
# Função para cadastrar livro
def cadastrar_livro(id):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    # Criando um dicionário com os dados do livro
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    # Adicionando o livro à lista de livros
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!")

# [EXIGÊNCIA DE CÓDIGO 4 de 8]
# Função para consultar livros
def consultar_livro():
    opcao = input("Escolha uma opção: 1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu: ")
    if opcao == "1":
        for livro in lista_livro:
            print(livro)
    elif opcao == "2":
        id_consulta = int(input("Digite o id do livro: "))
        for livro in lista_livro:
            if livro["id"] == id_consulta:
                print(livro)
                break
    elif opcao == "3":
        autor_consulta = input("Digite o autor do livro: ")
        for livro in lista_livro:
            if livro["autor"] == autor_consulta:
                print(livro)
    elif opcao == "4":
        return
    else:
        print("Opção inválida")

# [EXIGÊNCIA DE CÓDIGO 5 de 8]
# Função para remover livro
def remover_livro():
    id_remove = int(input("Digite o id do livro a ser removido: "))
    global lista_livro
    lista_livro = [livro for livro in lista_livro if livro["id"] != id_remove]
    print("Livro removido com sucesso.")

# [EXIGÊNCIA DE CÓDIGO 6 de 8]
# Loop principal do programa
while True:
    opcao = input("Escolha uma opção: 1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa: ")
    if opcao == "1":
        cadastrar_livro(id_global)
        id_global += 1
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Encerrando o programa. Obrigado por usar o sistema.")
        break
    else:
        print("Opção inválida")
2
