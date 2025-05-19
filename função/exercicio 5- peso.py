#crie uma função que receba dois parâmetros que serão o peso(kg) e a altura(m) de uma pessoa e retorne seu IMC.
#exercicio 5

def conta_imc (peso, altura) :
    imc_conta = peso / (altura * altura)
    return imc_conta

def classificacao (imc) :
    if imc <= 18.5:
        print("abaixo do peso")
    elif imc >= 18.5 <= 24.9:
        print("peso normal")
    elif imc >= 25:
        print("sobrepeso")
    elif imc >= 30:
        print("obesidade")
   
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = conta_imc(peso, altura)
print("seu imc é", imc)
classificacao(imc)
