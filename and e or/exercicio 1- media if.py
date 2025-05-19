num1 = int(input("digite uma nota de 0 a 100: "))
num2 = int(input("digite outra nota de 0 a 100: "))

if num1 and num2 <= 100:
    print("valido")
    
    soma = num1 + num2
    media = soma / 2
    print("o resultado da media é: ", media)

    if media >= 70:
        verifica = "aprovado"
    
    elif media >= 50:
        verifica = "recuperacao"
    
    elif media < 50:
        verifica = "reprovado"

    print("você esta: ", verifica)

else :
    print("invalido")
    
    