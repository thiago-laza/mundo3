'''
crie um programa que leia nome, sexo e idade
de varias pessoas, guardando os dados de cada
pessoa em um dicionario e todos os dicionarios
em uma lista. no final, mostre:
a)quantas pessoas foram cadastradas
b)a media de idade do grupo
c)uma lista com todas as mulheres
d)uma lista com todas as pessoas
com idade acima da media

programa

nome 
sexo
idade
quer continuar
nome
...

saida

o grupo tem ... pessoas
a media de idade e de ... anos
as mulheres cadastradas sao: ...
lista das pessoas que estao acima da media:

nome: ... ; sexo:... ; idade = ...
nome: ... ; sexo:... ; idade = ...
'''
pessoa = {}
pessoas = []
while True:
    nome = input('Nome: ')
    sexo = input('Sexo: ')
    idade = int(input('Idade: '))
    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade
    pessoas.append(pessoa)
    resp = input('Deseja continuar? [s/n]')
    if resp in 'Nn':
        break
print(pessoas)