print("despesas")

valor = 0
n_despesas = 0

while True:
    print("despesas")
    print("1 = valor da despesa")
    print("2 = quantidade e valor total da despesa")
    print("0 = sair")
    menu = int(input("o que você vai fazer hoje? "))
    if menu == 0:
        print("você saiu")
        break
    elif menu == 1:
        ad_valor = int(input("qual o valor? "))
        print("você adicionou", ad_valor, "reais em sua despesa")
        n_despesas += 1
        valor = ad_valor + valor
       
    elif menu == 2:
        print("você tem o total de ", n_despesas, "despesas, que somam", valor, "reais de despesas")
       
    else:
        print("ERRO")
