#crie uma funcao que calcula o valor do frete da seguinte forma:
#valor = (peso X 0.5) + (distancia x 0.1) + taxa_fixa

def calcular_frete (peso, distancia, taxa_fixa):
    valor = (peso * 0.5) + (distancia * 0.1) + taxa_fixa
    print("valor do frete é: ", valor)
    
peso = int(input("digite o peso: "))
distancia = int(input("digite a distancia: "))
taxa_fixa = 15
calcular_frete(peso, distancia, taxa_fixa)
