'''
Crie um programa que vai gerar cinco numeros aleatorios e colocar em
uma tupla. Depois disso, mostre a listagem de numeros gerados e tambem 
indique o menor e o maior valor que estao na tupla.
'''

import random

lista = []

for i in range(5):
    numeros = random.randint(1,10)
    lista.append(numeros)

maior = max(lista)
menor = min(lista)


print(f'Os 5 numeros gerados aleatoriamente sao: {lista}')
print(f'O menor numero da lista e: {menor}')
print(f'O maior numero da lista e: {maior}')


