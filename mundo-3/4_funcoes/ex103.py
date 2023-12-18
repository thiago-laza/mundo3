'''
Faca um programa que tenha uma funcao chamada ficha(), que receba dois parametros
opcionais o nome de um jogador e quantos gols marcou.

O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado
nao tenha sido informado corretamente.

Programa

nome do jogador = ...
numero de gosl = ...

saida:
-> o jogador NOME fez N gols no campeonato
obs: sem nome - > o jogador <desconhecido> fer N gols no campeonato
obs: sem gols - > o jogador NOME fez 0 gols no campeonanto
obs: sem gols sem nome -> o jogador <desconhecido> fez 0 gols no campeonato
'''
'''
MINHA SOLUCAO

def ficha(n=False, g=False):
    global resp_nome, resp_gols
    if not nome:
        resp_nome = '<desconhecido>'
    else:
        resp_nome = nome

    if not gols:
        resp_gols = 0
    else:
        resp_gols = gols

    return f'O jogador {resp_nome} fez {resp_gols} no campeonato.'




nome = input('Nome do jogador: ')
gols = input('Numero de gols: ')
print(ficha(nome,gols))
'''
def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
gols = input('Numero de gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    g = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome,gols)