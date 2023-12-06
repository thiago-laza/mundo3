'''
DESAFIO 087: Mais Sobre Matriz em Python

Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
"""

'''
print('Digite valores para preencher a matriz:')
print('0[_][_][_]\n1[_][_][_]\n2[_][_][_]\n  0  1  2')

matrix = [[],[],[]],[[],[],[]],[[],[],[]]
acu_total = 0
acu_c3 = 0
maior_l2 = 0
for l in range(3):
    for c in range(3):
        elemento = int(input(f'Digite o elemento da posicao {l},{c}: '))
        acu_total+=elemento
        if c == 2:
            acu_c3+=elemento
        if l == 1:
            if elemento > maior_l2:
                maior_l2 = elemento
        matrix[l][c].append(elemento)

print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}')
print(f'A soma de todos os valores digitados e {acu_total}')
print(f'A soma de todos os valores da terceira coluna e {acu_c3}')
print(f'O maior valor da segund linha e {maior_l2}')