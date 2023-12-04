"""
DESAFIO 084: Lista Composta e Análise de Dados

Faça um programa que leia nome e peso de várias pessoas, guardando tudo 
em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

obs: mais leve e o menor peso e mais pesada o maior peso
"""

'''
Minha tentaviva de solucao
obs: nao fiz as listas dos mais pesados e dos mais leves.
'''
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])#cria uma copia de temp sem ligacao
    temp.clear()
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break


print('-='*30)
print(f'{princ}')
print('-='*30) 
print(f'Ao todo, voce cadastrou {len(princ)} pessoas.')
print('-='*30)
print(f'O maior peso foi de {maior} kg.')
for p in princ:
    if p[1] == maior:
        print(p[0])
print('-='*30)
print(f'O menor peso foi de {menor} kg.')
for p in princ:
    if p[1] == menor:
        print(p[0]) 



    

