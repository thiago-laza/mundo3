'''
aprimore o exercicio 93 para que ele
funcione com varios jogadores, incluindo
um sistema de visualizacao do aproveitamento
de cada jogador.

programa

nome do jogador ...
quantas partidas ... jogou ...
gols na partida ...
...
quer continuar?
nome do jogador ...
quantas partidas ...
gols na partida ...
...
quer continuar? 
...

saida:

cod  nome   gols total
             []

mostrar os dados de qual jogador?

levantamento do jogador ...
no jogo ... fez ... gols
no jogo ... fez ... gols 
...

obs: codigo invalido -> erro
mostrar os dados de qual jogador?


obs: 999 para o programa.
'''
jogadores = []
while True:
    atleta = {}
    lista_gols = []

    atleta['nome'] = input('Nome do jogador: ')
    partidas = int(input('Numero de partidas: '))
    for p in range(partidas):
        gols = int(input(f'Numero de gols na partida {p+1}: '))
        lista_gols.append(gols)

    resp = input('Deseja cadastrar outro jogador? [s/n] ')
    if resp in 'Nn':
        break

print(lista_gols)



