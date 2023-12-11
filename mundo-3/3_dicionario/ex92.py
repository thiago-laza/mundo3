'''
crie um programa que leia nome, ano de 
nascimento e a carteira de trabalho e 
cadastre-os(com idade) em um dicionario
se por acaso a CTPS for diferente de zero,
o dicionario recebera tambem o ano de 
contratacao e o salrio. calcule e acrescente,
alem da idade, com quantos anos a pessoa vai se 
aposentar.

saida:

input
nome:
ano de nasc
ctps 
ano de contratacao
salario

saida prog
nome tem valor ...
idade tem valor ...
ctps tem valor ...
contratacao tem valor ...
salario tem valor ...
aposentadoria tem valor ...

obs: ctps zero

nome tem valor ...
idade tem valor ...
ctps tem valor 0

'''
inf = {}
nome = input('Nome: ')
inf['Nome'] = nome
nascimento = int(input('Ano de nascimento: '))
inf['Idade'] = 2023 - nascimento
ctps = int(input('Carteira de trabalho (0 nao tem): '))
inf['CTPS'] = ctps
if ctps == 0:
    print('=' * 20)
    for j,k in inf.items():
        print(f'{j} tem valor {k}')
else:
    contratacao = int(input('Ano de contratacao: '))
    inf['Contratacao'] = contratacao
    salario = float(input('Salario: R$ '))
    inf['Salario'] = salario
    inf['Aposentadoria'] = (2023-nascimento)+35
    print('=' * 20)
    for j,k in inf.items():
        print(f'{j} tem valor {k}')









