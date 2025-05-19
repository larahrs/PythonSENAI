#1 nome do produto e o preço
#2 aplique desconto de 5%
#3 exiba o novo preço do produto e quanto ele diminuiu



print("desconto do produto")

nome = input("escreve o nome do produto ")
preco = int(input("digite o preço do produto "))
resultado = preco / 5
resultado2 = preco - resultado

print("o desconto foi de: ", resultado, "o preco final é ", resultado2)