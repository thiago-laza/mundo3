'''
faca um programa que tenha uma funcao chamada
maior(), que recebe varios parametros com valores
inteiros.

seu programa tem que analisar todos os valores e dizer
qual e o maior deles.

PROGRAMA

[ ]foi passado 3 valores e o maior e o 7
[ ]foi passado 5 valores e o maior e 8
[ ]foi passado 1 valores e o maior e ...
[ ]nao foi passado nenhum valor e o mairo valor nao existe
'''
from time import sleep
def contador(*num):
    maior_valor = None
    lista_valores = []
    print('Analisando os valores passados...')
    sleep(0.5)
    for n in num:
        if maior_valor is None or n > maior_valor:
            maior_valor = n
        lista_valores.append(n)
    if len(lista_valores) == 0:
        sleep(0.5)
        print(f'{lista_valores} nao foi passado nenhum valor.')
        print('O maior valor nao existe.')
    else:
        sleep(0.5)
        print(f'{lista_valores} foi passado {len(lista_valores)} valores.')
        print(f'O maior valor informado foi {maior_valor}')
    print(20*'-')


contador(1,2,3)
contador(5,3,1,6,2)
contador()


