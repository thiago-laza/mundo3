'''
faca um programa que tenha uma funcao chamada
contador(), que receba tres parametros:inicio,fim
e passo e realize a contagem.

seu programa tem que realizar tres contagens atraves
da funcao criada:

a)de 1 ate 10 de 1 em 1
b)de 10 ate 0 de 2 em 2
c)uma contagem personalizada

PROGRAMA

a) aparece msg e os numeros
b) aparece msg e os numeros
c) pede inicio, fim e passo
   aparece msg e os numeros

obs: funcionar crescente e decrescente
obs: se o passo for 0 fica 1
'''
from time import sleep
def contador(inicio, fim, passo):
    print(f'Contegem de {inicio} ate {fim} de {passo} em {passo}')
    if passo < 0:
        passo*= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        while inicio <= fim:
            print(inicio ,end=' ')
            sleep(0.5)
            inicio+=passo
        print('Fim')
    else:
        while fim < inicio:
            print(inicio, end=' ')
            sleep(0.5)
            inicio-=passo
        print('Fim')


#contador(1,10,1)
#contador(10,0,2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)
