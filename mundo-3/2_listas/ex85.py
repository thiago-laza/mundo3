"""
DESAFIO 085: Listas com Pares e Ímpares

Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores 
pares e ímpares. No final, mostre os valores pares e ímpares 
em ordem crescente.
"""
'''
minha solucao
obs: criei mais de uma lista
numeros = []
pares = []
impares = []

for n in range(1,5):
    valores = int(input(f'Digite o {n}⁰ valor: '))
    if valores % 2 == 0:
        pares.append(valores)
        pares.sort()
    else:
        impares.append(valores)
        impares.sort()

numeros.append(pares[:])
numeros.append(impares[:])

print(numeros)
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')
'''
num = [[],[]]
#valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}o valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
        num[0].sort()
    else:
        num[1].append(valor)
        num[1].sort()

print(f'Todos os valores digitados: {num}')
print(f'Os valores pares sao: {num[0]}')
print(f'Os valores impares sao: {num[1]}')




    
    




