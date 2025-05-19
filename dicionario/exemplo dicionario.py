#criar
aluno = {
    "nome": "Larah",
    "idade": 16,
    "altura": 1.59,
    "matriculado": True
}

#print(aluno)

#adicionar campo
aluno ["peso"] = 70
#print(aluno)

#alterar campo
aluno["idade"] = 17

#print(aluno)

#deletar campo
del aluno["altura"]

#print(aluno)

#verificar
if "altura" in aluno:
    print("altura existente")
else:
#    print("altura inexistente")
    print()

#exibir
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
#    print()

objeto = {
    "nome": "armario",
    "altura": 1.90,
    "cor": "cinza",
    
}
print(objeto)

objeto2 = {
    "nome": "geladeira",
    "altura": 1.90,
    "cor": "branco",
    
}
print(objeto2)

objeto3 = {
    "nome": "fogao",
    "altura": 1.30,
    "cor": "preto",
    
}
print(objeto3)

#exibir uma lista de dicionarios
lista_objeto = [objeto, objeto2, objeto3]

        #escolhendo os campos
for objeto in lista_objeto:
    print(f"{objeto['nome']}")
        #exibindo todos
for objeto in lista_objeto:
    for chave, valor in objeto.items():
        print(f"{chave} - {valor}")
    print()
    
