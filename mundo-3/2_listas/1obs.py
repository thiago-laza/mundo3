'''
lista = [2,3,4,5]
lista.append(6)
print(lista)
lista.insert(0,7)
print(lista)
del lista[3]
print(lista)
lista.pop(2)
print(lista)
lista.remove(7)
print(lista)
lista.pop()
print(lista)
-------------------------
valores = list(range(4,11))
print(valores)
--------------------------
valores = [4,2,6,1]
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
-------------------------
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}')
--------------------------

'''
a = [2,3,4,5]
b = a #ligacao entre as listas, modificar uma modifica a outra.
b = a[:]#faz uma copia.
b[2] = 7
print(a)
print(b)


