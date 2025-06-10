#faça uma funcao que verifica se um numero é positivo ou negativo
#e retorne true ou false

def verificar_positivo (numero):
    if numero < 0:
        print("esse numero é negativo")
        return False

    elif numero > 0:
        print("esse numero é positivo")
        return True


numero = int(input("digite um numero: "))
verificar_positivo (numero)