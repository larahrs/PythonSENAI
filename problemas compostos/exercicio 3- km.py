# quanto custa encher o tanque de um carro que tem 50l, esta com 20l e o combustivel é de R$5,80
# descobrir quantos litros faltam para encher
# fazer 50 - 20
# para descobrir o custo do combustivel
# fazer 30 * 5,80
# exibir o custo

capacidade = int(input("digite a capacidade "))
combustivel = int(input("digite quantos litros de combustivel tem "))
subtracao = capacidade - combustivel

preco = float(input("digite quanto custa o litro do combustivel "))
custo = subtracao * preco
print("o custo sera ", custo)
