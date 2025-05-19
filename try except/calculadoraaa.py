print("Calculadora")

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


#exercicio 3.2

def menu_calculadora():
    print("Calculadora")
    print("Para a adição, digite 0.1")
    print("Para a subtração, digite 0.2")
    print("Para a multiplicação, digite 0.3")
    print("Para a divisão, digite 0.4")
    print("Para todas as opções anteriores, digite 0.5")
    
def soma(n1, n2):
    return n1+n2

def subtracao(n1, n2):
    return n1-n2

def multiplicacao(n1, n2):
    return n1*n2

def divisao(n1, n2):
    return n1/n2

def todas_opcoes(n1, n2):
    print("o resultado da soma é ", soma(n1, n2))
    print("o resultado da subtração é ", subtracao(n1, n2))
    print("o resultado da multiplicação é ", multiplicacao(n1, n2))
    print("o resultado da divisão é ", divisao(n1, n2))
def calculo(n1, n2, operacao):
    if operacao == "0.1":
        print("o resultado da soma é",soma(n1, n2))
    elif operacao == "0.2":
        print("o resultado da subtração é", subtracao(n1, n2))
    elif operacao == "0.3":
        print("o resultado da multiplicação é", multiplicacao(n1, n2))
    elif operacao == "0.4":
        print("o resultado da divisão é", divisao(n1, n2))
    elif operacao == "0.5":
        tudo(n1, n2)
    else:
        print("Erro, Operação não reconhecida")

menu_calculadora()

while True:
    try:
        operacao = input("Digite a operação: ")
        break
        
    except ValueError:
        print("Digite somente o número referente a operação")

while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        break
    
    except ValueError:
        print("Digite apenas o número Ex:10")

while True:
    try:
        n2 = int(input("Digite o segundo número: "))
        
    
    except ValueError:
        print("Digite apenas o número Ex:09")

calculo(n1, n2, operacao)