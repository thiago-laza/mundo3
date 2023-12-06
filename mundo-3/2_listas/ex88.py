"""
DESAFIO 088: Palpites Para a Mega Sena

Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
import random

palpite = []
jogo = []


jogos = int(input('Quantos jogos deseja gerar? '))

for i in range(jogos):
    for i in range(6):
        numeros = random.randint(1,60)
        palpite.append(numeros)
    jogo.append(palpite[:])
    palpite.clear()

print(f'Os {jogos} jogos sao: {jogo}')
    
   
   



