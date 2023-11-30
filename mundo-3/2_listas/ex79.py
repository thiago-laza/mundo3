'''
Crie um programa onde o usuario possa digitar varios valores numericos
e cadastre-os em uma lista. caso o numero ja exista la dentro, ele
nao sera adicionado. no final, serao exibidos todos os valores unicos
digitados, em ordem crescente.
'''

'''
Minha solucao

lista = []

while True:
    numero = int(input('Digite um numero: '))
    if numero not in lista:
        print('Numero adicionado com sucesso.')
        lista.append(numero)
    else:
        print('Numero duplicado, nao sera adicionado.')
    resp = input('Deseja adicionar outro numero [s/n]?: ')
    if resp == 'n':
        break

lista.sort()
print(f'Voce digitou os numeros {lista}')

'''

numeros = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Voce digitou os valores: {numeros}.')

