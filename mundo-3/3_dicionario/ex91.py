'''
crie um programa onde 4 jogadores joguem um
dado e tenham resultados aleatorios. guarde
esses resultados em um dicionario em ordem, 
sabendo que o vencedor tirou o maior numero
no dado.

saida:

valores sorteados
o jogador 1 tirou ...
o jogador 2 tirou ...
o jogador 3 tirou ...
o jogador 4 tirou ...
ranking dos jogadores
o 1o lugar: jogador ... com ...
o ...
'''
from random import randint
from  time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
        }
ranking = []

for j,k in jogo.items():
    print(f'O {j} tirou {k} no dado.')
    sleep(1)

print('RANKIGN')
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}o lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)

