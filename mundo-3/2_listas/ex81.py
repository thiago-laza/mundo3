'''
crie um programa que vai ler varios numeros e colocar em uma lista.
depois disso, mostre:
a)quantos numeros foram digitados
b)a lista de valores ordenada de forma decrescente
c)se o valor 5 foi digitado e esta ou nao na lista
'''

'''
Minha solucao
obs: nao coloquei  a lista em ordem decrescente.

lista = []
cont = 0
resp = 's'

while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    cont+=1
    resp = input('Deseja continuar [s/n]: ')
    if resp == 'n':
        break

print(f'Os numeros digitados foram {lista}')
print(f'Foram digitados {cont} numeros.')

if 5 in lista:
    print('O numero 5 foi digitado e esta na lista.')
else:
    print('O numero 5 nao foi digitado e nao esta na lista.')

'''

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break


print(valores)
print(f'Voce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'A os valores em ordem decrescente sao {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 nao faz parte da lista.')


