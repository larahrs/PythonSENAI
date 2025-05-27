def cadastro (isbn, titulo, autor, categoria, ano_de_publicacao):
    livro = {
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "ano de publicacao": ano_de_publicacao,
    }
    livros.append(livro)
    
livros = []


while True:
    print("biblioteca")
    print("")

    print("[1] - cadastro dos livros ")
    print("[2] - exibir livros cadastrados ")
    print("[3] - exibir quantidade total de livros registrados ")
    print("[4] - exibir lista com os titulos cadastrados ")
    print("[0] - sair")
    print("")
    
    escolha = int(input("digite sua escolha: "))
    if escolha == 0:
        print("você saiu")
        break
    
    elif escolha == 1:
        isbn = int(input("digite o isbn(unico): "))
        titulo = input("digite o titulo do livro: ")
        autor = input("digite o autor do livro: ")
        categoria = input("digite a categoria do livro: ")
        ano_de_publicacao = int(input("digite o ano de publicacao: "))
    
        cadastro(isbn, titulo, autor, categoria, ano_da_publicacao)
        print("cadastro do livro feito ")
    
    elif escolha == 2:
        for livro in livros:
            for chave, valor in livro.items():
                print(f"{chave} - {valor}")
                
    elif escolha == 3:
        print(len(livros))
           
    elif escolha == 4:
        for livro in livros:
            print(livros[1])

