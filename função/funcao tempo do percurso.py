#faca uma funcao que receba uma distancia em km e uma velocidade, calcule quanto tempo levara para fazer esse percurso?

def calcular_percurso (distancia, velocidade):
    tempo = distancia / velocidade
    print("o tempo é", tempo)
     
distancia = int(input("qual a distancia? "))
velocidade = int(input("qual a velocidade? "))
calcular_percurso(distancia, velocidade)