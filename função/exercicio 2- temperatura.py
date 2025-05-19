#crie uma função que receba uma temperatura em graus Celsius como parâmetro e retorne o valor convertido para Fahrenheit e outra para Kelvin.
#exercicio 2- temperatura
def celsius_para_fahrenheit(graus):
    conversao_fahrenheit = graus * 1.8 + 32
    return conversao_fahrenheit 


def celsius_para_kelvin(kelvin):
    conversao_kelvin = graus + 273
    return conversao_kelvin
    
def mostrar_conversao(graus):
    print("o resulatdo é: ", celsius_para_fahrenheit(graus), "em fahrenheit")
    print("o resultado é: ", celsius_para_kelvin(graus), "em kelvin")
    
graus = float(input("quantos graus esta? "))

mostrar_conversao(graus)   