'''
faca um programa que leia 5 valores numericos e guarde em uma lista.
no final, mostre qual foi o maior e o menor valor digitado e suas 
respectivas posicoes na lista.
'''

'''
Minha solucao

lista = []

for i in range(1,6):
    numero = int(input(f'Digite o {i}⁰ valor: '))
    lista.append(numero)

maior = max(lista)
posicao_maior = lista.index(maior)
menor = min(lista)
posicao_menor = lista.index(menor)

print(f'Os valores digitados foram {lista}')
print(f'O maior valor digitado foi {maior} na posicao {posicao_maior}')
print(f'O menor valor digitado foi {menor} na posicao {posicao_menor}')

#obs: nao indica o menor ou maior quando aparece mais de uma vez.
'''

listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posicoes ', end=' ')
for i,v in enumerate(listanum):
    if v == maior:
        print(f'{i}', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posicoes ', end=' ')
for i,v in enumerate(listanum):
    if v == menor:
        print(f'{i}', end=' ')
print()