#exercicio 6:
#solicite ao usuário três números inteiros e mostre o maior deles.

print("qual é o maior entre os números inteiros")

n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite um segundo numero diferente: "))
n3 = int(input("digite um terceiro número diferente: "))

if n1>n2:
    if n1>n3:
        print(n1, "é o maior número")
elif n3>n1:
     if n3>n2:
        print(n3, "é o maior número")
elif n2>n1:
     if n2>n3:
         print(n2, "é o maior número")
