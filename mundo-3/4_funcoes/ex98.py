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
def contador(inicio, fim, passo):
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=' ')
            inicio+=passo
    else:
        print()
        while fim < inicio:
            print(inicio, end=' ')
            inicio-=passo

print('De 1 ate 10 de 1 em 1:',end=' ')
contador(1,10,1)
print('\nDe 10 ate 0 de 2 em 2:')
contador(10,0,2)
print()
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)
