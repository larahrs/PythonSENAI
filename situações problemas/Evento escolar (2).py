nomes = []

while True:
    print("menu")
    print("")
    print("[1]- cadastrar nomes dos participantes ") 
    print("[2]- exibir o total de inscritos (quantidade de nomes na lista) ")
    print("[3]- exibir a lista de nomes em ordem alfabética ")
    print("[4]- permitir a consulta de um nome ")

    menu = int(input("escolha uma opção: "))
    
    if menu == 1:
        nome = str(input("digite seu nome completo: "))
        if nome in nomes:
            print("este nome ja esta na lista ")
        else:
            nomes.append(nome)
            print("seu nome foi adicionado ")
    
    elif menu == 2:
        print(len(nomes))
        
    elif menu == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)

    elif menu == 4:
        nome = str(input("digite um nome para verificar se está presente:"))
        if nome in nomes:
            print("nome encontrado!")
            remover = input("deseja remove-lo? s/n?")
            nomes.remove(nome)
            print("nome removido!")
            continuar = input("gostaria de avançar? s/n?")
            if continuar == "nao":
                print("fim")
                break
                   
        else:
            print("nome nao encontrado! ")
    else:
        print("nome não encontrado")
        print("[1] sim")
        print("[2] não")
        menu2 = int(input("deseja adicioná-lo? "))
        if menu2 == 1:
            nomes.append()
            print("seu nome foi adicionado")
            
            


