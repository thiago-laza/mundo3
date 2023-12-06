"""
DESAFIO 086: Matriz em Python

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com 
valores lidos pelo teclado.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2

No final, mostre a matriz na tela, com a formatação correta.
"""
print('Digite valores para preencher a matriz:')
print('0[_][_][_]\n1[_][_][_]\n2[_][_][_]\n  0  1  2')

matrix = [[],[],[]],[[],[],[]],[[],[],[]]

for l in range(3):
    for c in range(3):
        elemento = int(input(f'Digite o elemento da posicao {l},{c}: '))
        matrix[l][c].append(elemento)

print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}')
