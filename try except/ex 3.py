import inputs

def calculo(n1, n2):
    print("Os resultados são :", adicao(n1,n2) ,"na adição, " , subtracao (n1,n2) ,"na subtração, ", multiplicacao (n1,n2) , "na multiplicação e " ,  divisao (n1,n2) , "na divisão")


#exercicio 3.1

def adicao (n1 , n2):
    conta_soma = n1 + n2
    return conta_soma

def subtracao (n1 , n2):
    conta_subtração = n1 - n2
    return conta_subtração

def multiplicacao (n1 , n2):
    conta_multiplicação = n1 * n2
    return conta_multiplicação

def divisao (n1 , n2):
    conta_divisão = n1 / n2
    return conta_divisão
def tudo(n1, n2):
    conta_soma = n1+n2
    conta_subtracao = n1 - n2
    conta_multiplicacao = n1*n2
    conta_divisao = n1 / n2
    print(conta_divisao)
    print(conta_multiplicacao)
    print(conta_soma)
    print(conta_subtracao)
    


#exercicio 3.2

def menu_calculadora():
    print("Calculadora")
    print("[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Opções anteriores")
   
def soma(n1, n2):
    return n1+n2

def subtracao(n1, n2):
    return n1-n2

def multiplicacao(n1, n2):
    return n1*n2

def divisao(n1, n2):
    return n1/n2

def todas_opcoes(n1, n2):
    print("O resultado da soma é ", soma(n1, n2))
    print("O resultado da subtração é ", subtracao(n1, n2))
    print("O resultado da multiplicação é ", multiplicacao(n1, n2))
    print("O resultado da divisão é ", divisao(n1, n2))
def calculo(n1, n2, operacao):
    if operacao == 1:
        print("O resultado da soma é",soma(n1, n2))
    elif operacao == 2:
        print("O resultado da subtração é", subtracao(n1, n2))
    elif operacao == 3:
        print("O resultado da multiplicação é", multiplicacao(n1, n2))
    elif operacao == 4:
        print("O resultado da divisão é", divisao(n1, n2))
    elif operacao == 5:
        tudo(n1, n2)
    else:
        print("Erro")
menu_calculadora()

operacao = inputs.input_int("Digite um número: ")
        


n1 = inputs.input_int("Digite o primeiro número: ")
    
   
n2 = inputs.input_int("Digite o segundo número: ")
       

calculo(n1, n2, operacao)