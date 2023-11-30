'''
crie um programa que vai ler varios numeros e colocar em uma lista.
depois disso, crie duas listas extras que vao conter apenas os valores
pares e os valores impares digitados, respectivamente. no final mostre
o conteudo das tres listas geradas.
'''

'''
Minha solucao

lista_numero = []
lista_par = []
lista_impar = []
resp = 's'
cont = 0

while True:
    numero = int(input('Digite um numero: '))
    lista_numero.append(numero)
    if lista_numero[cont] % 2 == 0:
        lista_par.append(lista_numero[cont])
    else:
        lista_impar.append(lista_numero[cont])
    cont+=1
    resp = input('Deseja continuar[s/n]? ')
    if resp == 'n':
        break
    

    

print(f'Os numeros digitados foram: {lista_numero}')

if len(lista_par) == 0:
    print('Nao foram digitados nenhum numero par.')
else:
    print(f'Os numeros pares digitados foram: {lista_par}')

if len(lista_impar) == 0:
    print('Nao foram digitados nenhum numero impar.')
else:
    print(f'Os numeros impares digitados foram: {lista_impar}')
'''

num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um numero: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa e {num}')
print(f'A lista de pares e {pares}')
print(f'A lilsta de impares e {impares}')

