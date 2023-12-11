'''
faca um programa que leia nome e a media
de um aluno, guardando tambem a situacao
em um dicionario. no final, mostre o conteudo
estruturado na tela.

saida:
nome e igual a ...
media e igual a ...
media e igual a ...
situacao e igual a ...
'''

cadastro = {}

nome = input('Nome: ')
cadastro['nome'] = nome
media = float(input('Media: '))
cadastro['media'] = media

if media < 7:
    situacao = 'Reprovado'
else:
    situacao = 'Aprovado'
cadastro['situacao'] = situacao

for i,j in cadastro.items():
    print(f'{i} e igual a {j}')
