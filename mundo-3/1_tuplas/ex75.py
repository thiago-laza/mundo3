'''
desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. no final mostre:
a)quantas vezes apareceu o valor 9
b)em que posicao foi digitado o primeiro valor 3
c)quais foram os numeros pares.
'''

valores = []
pares = []

for i in range(1,5):
    numero = int(input(f'Informe o {i} numero: '))
    valores.append(numero)
    if numero % 2 == 0:
        pares.append(numero)

print(f'Os numeros digitados foram: {valores}')
print(f'O numero 9 apareceu {valores.count(9)} vez(s)')

if 3 in valores:
    print(f'O numero 3 foi digitado pela primeira vez na posicao {valores.index(3)}')
else:
    print('O numero 3 nao foi digitado em nenhuma posicao.')

if len(pares) == 0:
    print('Nao foram digitados nenhum numero par.')
else:
    print(f'Os numeros pares digitados foram {pares}')

