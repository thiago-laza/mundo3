'''
faca um programa que tenha uma funcao chamada
area, que receba as dimensoes de um terreno
retangular(largura e comprimento) e mostre
a area do terreno.
PROGRAMA:
larguara = ...
comprimento = ...
a area de um terreno lar x com e de ... m2
'''
def area(l,c):
    a = l * c
    print(f'A area de um terreno {l}m x {c}m e de {a}m2')


l = float(input('Informe a largura do tereno (m): '))
c = float(input('Informe o comprimento do terreno (m): '))
area(l,c)


