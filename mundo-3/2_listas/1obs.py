'''
---------------------
PARTE 1
---------------------
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
'''
a = [2,3,4,5]
b = a #ligacao entre as listas, modificar uma modifica a outra.
b = a[:]#faz uma copia.
b[2] = 7
print(a)
print(b)
'''
'''
---------------------------------------------
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}')
----------------------------------------------------
'''
'''
PARTE 2
'''

'''
pessoas = [['pedro',25],['maria',19],['joao',32]]

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
'''

'''
teste = list()
teste.append('thiago')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'fabiana'
teste[1] = 42
galera.append(teste[:])
print(galera)
'''
'''
galera = [['joao',19],['ana',33],['joaquim',13],['maria',45]]
for pessoa in galera:
    print(pessoa)
for pessoa in galera:
    print(pessoa[0])
for pessoa in galera:
    print(pessoa[1])
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
'''
'''
galera = list()
dado = list()
cont_mairo = 0
cont_menor = 0
for c in range(3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for pessoa in galera:
    if pessoa[1] >=18:
        print(f'{pessoa[0]} e maior de idade.')
        cont_mairo+=1
    else:
        print(f'{pessoa[0]} e menor de idade.')
        cont_menor+=1
print(f'Temos {cont_mairo} pessoas maior de idade e {cont_menor} pessoas menor de idade.')
'''
pessoas = [['pedro',25],['maria',19],['joao',32]]

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])








