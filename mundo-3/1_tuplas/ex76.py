'''
crie um programa que tenha uma tupla unica com nomes de produtos e seus
respectivos precos, na sequencia.

no final, mostre uma listagem de precos, organizadondo os dados em forma tabular.

listagem = ('pao',1,'leite',5,'carne',21)

saida:

-----------------------------------------
          listagem de precos
-----------------------------------------
pao .............................R$  1,00
leite ...........................R$  5,00
carne............................R$ 21,00
-----------------------------------------
'''

listagem = ('Pao',1,'Leite',5.5,'Cafe',6.4,'Biscoito',5.45,'Pneu',365.76)

print('-'*32)
print(f'{"LISTA DE PRECOS":^30}')
print('-'*32)
for i in range(0,len(listagem),2):
    print(f'{listagem[i]:.<20}  R$ {listagem[i+1]:>7.2f}')
print('-'*32)


