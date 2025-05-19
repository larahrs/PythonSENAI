# vamos calcular a area do hexagono
# area de hexagono = 6 (lados do hexagono) * At (area do triangulo)
# area do triangulo = l2.3**0.5 / 4
# para calcular area de triangulo equilatero
# obter o valor do lado do triangulo
# o valor eleva a 2 (multiplicar por el mesmo)
# multiplicar o resultado da multiplicacao por raiz de 3
# resultado da multiplicacao dividi por 4
# resultado da divisao multiplicar por 6

print("area do hexagono")
lado = int(input("digite o valor do lado do triangulo"))
lado2 = lado * lado
raiz = round(3**0.5, 2)
mult = raiz * lado2
divisao = mult / 4
area = round(divisao * 6, 2)
print("a area do hexagono é", area)
