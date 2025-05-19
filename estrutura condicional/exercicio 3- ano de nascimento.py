#exercicio 3:
#solicite o ano de nascimento de uma pessoa, calcule a idade e verifica se a pessoa é maior ou menor de idade e exiba uma mensagem correspondente.

ano_nascimento = int(input("Digite o ano de nascimento "))

subtracao = 2025 - ano_nascimento

if subtracao < 18:
    print("menor de idade")
else:
    print("maior de idade")