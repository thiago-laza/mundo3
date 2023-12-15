'''
faca um programa que tenha uma lista chamada numeros
e duas funcoes chamadas sorteia() e somaPar(). a primeira
funcao vai sortear 5 numeros e vai coloca-los dentro da lista
e a segunda funcao vai mostrar a soma entre todos os
valores pares sorteados pela funcao anterior.

PROGRAMA:

sorteando 5 valores: ...
a soma dos valores pares de [...] e igual a SOMA.

'''
import random
lista = []

def sorteia():
    for n in range(5):
        n = random.randint(0,10)
        lista.append(n)
    print(lista)

def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma+=n
    print(f'A soma dos valores pares de {lista} e igual a {soma}')


sorteia()
soma_par(lista)











