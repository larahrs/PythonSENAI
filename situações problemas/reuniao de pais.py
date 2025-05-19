print("reunião de pais")
print("")

print("[1] - cadastrar os nomes")
print("[2] - exibir o total de pais")
print("[3] - exibir a lista de nomes em ordem alfabetica")
print("[4] - confirmação de presença")
print("[6] - sair")

nomes=[]
presentes=[]
ausentes=[]

while True:
    opcao=int(input("digite sua escolha: "))
    print("")


    if opcao == 1:
        nome=input("digite o nome que deseja cadastrar: ")
        if nome in nomes:
            print("nome ja cadastrado")
        else:
            nomes.append(nome)
            print("nome cadastrado com sucesso")
    
    elif opcao == 2:
        print("o total de pais são:", len(nomes))
        
    elif opcao == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
            
    elif opcao == 4:
       nome=input("digite um nome para verificar se está presente:")
       if nome in nomes:
           presentes.append(nome)
           print("nome está em nossa lista de presentes")
       else:
           ausentes.append(nome)
           print("nome está em nossa lista de ausentes")
    
    elif opcao == 5:
        print("lista de presentes: ")
        for item in presentes:
            print(item)
        print("")
        print("lista de ausentes: ")
        for item in ausentes:
            print(item)
        
    elif opcao == 6:
        print("você saiu")
        break
    
    else:
        print("essa opção não existe ")