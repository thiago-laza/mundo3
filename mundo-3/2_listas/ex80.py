'''
crie um programa onde o usuario possa digitar cinco valores numericos
e cadastre-os em uma lista, na na posicao correta de insercao(sem usar
sort()). no final mostre a lista ordenada na tela.
'''
'''
Minha solucao(nao foi finalizado)

lista = []

for i in range(1,6):
    numero = int(input(f'Digite o {i} numero: '))
    lista.append(numero)
    
    
print(lista)
'''

lista = []
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:#o primeiro e inserido em 0 e o maior na ultima.
        lista.append(num)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'Adicionado na posicao {pos}')
                break
            pos+=1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
    
