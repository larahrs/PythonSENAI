peso = float(input("digite o peso "))
altura = float(input("digite a altura "))
imc = peso / altura * altura

if imc <= 18.5:
    print("abaixo do peso")
elif imc >= 18.5 <= 24.9:
    print("peso normal")
elif imc >= 25:
    print("sobrepeso")
elif imc >= 30:
    print("obesidade")