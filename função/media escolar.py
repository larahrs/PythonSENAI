print("cadastro")

def menu():
    print("[1] - cadastro do nome")
    print("[2] - calculo da media")
    print("[3] - resultado final")
    print("[0] - sair")
def calcular_media(n1, n2, n3):
    media = (n1+n2+ n3) / 3
    return media
def cadastrar_aluno():
    nome = input("digite o nome: ")
    n1 = int(input("digite sua primeira nota: "))
    n2 = int(input("digite sua segunda nota: "))
    n3 = int(input("digite sua terceira nota: "))
    aluno = {
    "nome": nome,
    "n1": n1,
    "n2": n2,
    "n3": n3,
    }
    m = calcular_media(n1, n2, n3)
    s = verificar_situacao(m)
    aluno["media"] = m
    aluno["situacao"] = s
    
    alunos.append(aluno)
    


def verificar_situacao(media):
    if media >= 7:
        return "aprovado" 
   
    elif media >= 5 and media < 7:
        return "recuperacao"
    
    else:
        return "reprovado"
    

def mostrar_relatorio(alunos):
    for aluno in alunos:
        for chave, valor in aluno.items():
            print(f"{chave} - {valor}")
            
alunos = []
            
while True:
    menu()
    escolha = int(input("digite sua escolha: "))
    if escolha == 0:
        print("voce saiu")
        break
    
    elif escolha == 2:
        verificar_situacao(calcular_media(n1, n2, n3))
        print("media calculada")
        
    elif escolha == 1:
        cadastrar_aluno()
        print("nome cadastrado ")
        
    elif escolha == 3:
        mostrar_relatorio(alunos)
        
    else:
        print("essa escolha nao existe")