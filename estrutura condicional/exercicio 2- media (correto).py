#exercicio 2:
#solicite duas notas de um aluno e calcule a média. Se a média for maior ou igual a 70, o aluno está aprovado. Caso contrário, está reprovado.

n = int(input("digite uma nota "))
n2 = int(input("digite outra nota "))
soma = n + n2
media = soma / 2
print("resultado da media: ", media)

if media > 70 :
    verifica = "aprovado"
   
elif media < 70 :
    verifica = "reprovado"
   
print("seu resultado foi " , verifica) 