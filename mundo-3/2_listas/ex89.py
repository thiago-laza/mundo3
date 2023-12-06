"""
DESAFIO 089: Boletim com Listas Compostas

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""

cadastro = []
temp = []

while True:
    nome = input('Nome: ')
    temp.append(nome)
    nota1 = float(input('Nota 1: '))
    temp.append(nota1)
    nota2 = float(input('Nota 2: '))
    temp.append(nota2)
    cadastro.append(temp[:])
    temp.clear()

    resp = input('Deseja cadastrar mais um estudante? ')
    if resp in 'Nn':
        break

for i in range(len(cadastro)):
    media = (cadastro[i][1] + cadastro[i][2])/2
    print('-='*20)
    print(f'Estudante {i+1}: {cadastro[i][0]} ---- Media: {media}')
    print('-='*20)

while True:
    informacao = int(input('Para saber as notas do estudante, informe o numero: '))
    print(cadastro[informacao-1])
    resp2 = input('Deseja continuar? [S/N] ')
    if resp2 in 'Nn':
        break




