'''
Crie um programa chamado moeda.py que tenha as funcoes incorporadas
aumentar(), diminuir(), dobro() e metade().

Faca tambem um programa que importe asse modulo e use algumas funcoes
'''
from ex107_p import moeda
p = float(input('Digite o preco: R$ '))
print(f'A metade de {p} e {moeda.metade(p)}')
print(f'O dobro de {p} e {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p)}')