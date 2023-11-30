"""
DESAFIO 084: Lista Composta e Análise de Dados

Faça um programa que leia nome e peso de várias pessoas, guardando tudo 
em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

obs: mais leve e o menor peso e mais pesada o maior peso
"""

lista = []
dados = []
menor = 0
maior = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Altura: ')))
    lista.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar? [S/N] ')
    if resp in 'Nn':
        break

print(lista)
print(f'Foram cadastradas {len(lista)} pessoas.')


    



    

