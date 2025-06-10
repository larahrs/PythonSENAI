#a temperatura ideal para a qualidade do ar é entre 20C e 22C no inverno e 23C e 26C no verao
#a umidade ideal para a saude humana deve estar entre 40% e 55% no inverno e 40% e 65% no verao
#faca uma funcao que verifica a qualidade do ar com base nesses dados

def verificar_qualidade(temperatura, umidade, estacao):
    
    if estacao == "inverno":
        if temperatura >= 20 and temperatura <= 22:
            if umidade >= 40 and umidade <= 55:
                print("ideal para o inverno")
            else:
                print("nao esta ideal")

               
    elif estacao == "verao":
        if temperatura >= 23 and temperatura <= 26:
            if umidade >= 40 and umidade <= 65:
                print("ideal para o verao")
            else:
                print("nao esta ideal")
        
temperatura = int(input("digite uma temperatura: "))
umidade = int(input("digite a umidade: "))
estacao = str(input("digite a estacao: "))
verificar_qualidade(temperatura, umidade, estacao)

