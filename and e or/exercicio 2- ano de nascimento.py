ano1 = int(input("digite seu ano de nascimento: "))
idade = 2025 - ano1
print("sua idade é: ", idade)

if idade < 10:
    verifica = "criança"
    
elif idade <= 17:
    verifica = "adolescente"
    
elif idade <= 59:
    verifica = "adulto"
    
elif idade >= 60 and idade <= 116:
    verifica = "idoso"
    
print("vc é: ", verifica)