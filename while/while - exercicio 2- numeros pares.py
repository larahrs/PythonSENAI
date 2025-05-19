#solicite um numero ao usuario
num = int(input("digite um numero par: "))
quantidade = 0

print(num)

#exiba todos os numeros pares e a quantidade deles ate o numero solicitado
while True:
    num = num - 1
    if num % 2 == 0:
        print(num)
        quantidade = quantidade + 1
    elif num <= 0:
        print("a quantidade de numeros pares é: ", quantidade + 1)
        break