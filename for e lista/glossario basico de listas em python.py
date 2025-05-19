#passo 1:
objetos = ["cadeira", "regua", "mochila", "lousa", "mesa"]

#passo 2:
objetos.append("borracha")

#passo 3:
print(objetos[1])

#passo 4:
print(objetos.pop(1))

#passo 5:
print(len(objetos))

#passo 6:
for objeto in objetos:
    print(objeto)

#passo 7:
if "cadeira" in objetos:
    objetos.remove("cadeira")
    
else:
    objetos.append("cadeira")
    
#passo 8:
print(objetos)
print(objetos.sort())
print(objetos)

#passo 9:
print(objetos[0])
print(objetos[len(objetos) -1])

#passo 10:
objetos.clear()

