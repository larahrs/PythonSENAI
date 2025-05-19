#exercicio 1:
#solicite um número ao usuário e verifica se o número é positivo ou negativo e exiba uma mensagem positivo ou negativo

numero = int(input("digite um número: "))

if numero < 1:
    verifica = "negativo"
   
elif numero > 1:
    verifica = "positivo"
   
print("o número é: ", verifica)