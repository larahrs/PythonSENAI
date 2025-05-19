#solicite um numero ao usuario
num = int(input("digite um numero: "))

#faça uma contagem regressiva a partir desse numero
while True:
    print(num)
    num -= 1
    if num <= 0:
        break