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

cadastro = []
total_pessoas = 0
soma_idades = 0
mulheres = []
acima_media = []

while True:
    pessoa = {}

    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] =  input('Sexo [f/m]: ')
    pessoa['idade'] = int(input('Idade: '))

    cadastro.append(pessoa)
    total_pessoas+=1
    soma_idades+=pessoa['idade']

    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa)

    resp = input('Deseja continuar? [s/n] ')
    if resp in 'Nn':
        break

media_idade = soma_idades / total_pessoas

for pessoa in cadastro:
    if pessoa['idade'] > media_idade:
        acima_media.append(pessoa)

print(f'A) O grupo total tem {total_pessoas} pessoas.')
print(f'B) A media de idade do grupo e de {media_idade} anos.')
print('C) Lista de mulheres:')
for mulher in mulheres:
    print(f'{mulher["nome"]} {mulher["idade"]} anos.')
print('As pessoas com idade acima da media sao:')
for pessoa in acima_media:
    print(f'{pessoa["nome"]} {pessoa["idade"]} anos.')



