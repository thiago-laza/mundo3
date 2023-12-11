'''
crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou.
depois vai ler a quantidade de gols feitos em cada
partida. no final, tudo isso sera guardado
em um dicionario, incluindo o total de gols
feitos durante o campeonato.

programa

nome 
quantas partidas ..
quantos gosl fez na partida ..
...

saida:

o campo nome tem valor ...
o campo gols tem valor [...]
o campo total tem valor ...

o jogador ... jogou ... partidas
na partida 0, fez ... gols
na partida 1, fez ... gols
...
foi um total de ... gols.
'''
inf = {}
lista_gols = []

nome = input(('Nome do jogador: '))
inf['nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou? '))

acu = 0
for p in range(partidas):
    gols = int(input(f'Quantos gols na partida {p}? '))
    acu+=gols
    lista_gols.append(gols)
inf['gols'] = lista_gols
inf['total'] = acu

print(('='*50))
print((inf))

print(('='*50))
for j,k in inf.items():
    print(f'O campo {j} tem valor {k}')

print(f'O jogador {nome} jogou {partidas} partidas.')
for j,k in enumerate(lista_gols):
    print(f'Na partida {j}, fez {k} gols.')
print(f'Foi um total de {acu} gols.')




