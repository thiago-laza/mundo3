'''
Crie um programa que tenha uma funcao fatorial() que receba dois parametros
o primeiro que indique o numero a calcular e o outro chamado show que sera
um valor logico(opcional) indicando se sera mostrado ou nao na tela o processo
de calculo do fatorial.

Programa:

print(n) -> resultado
print(n,show=True) -> n.(n-1) ... resultado
obs:criar help da function
'''

'''
MINHA SOLUCAO

def fatorial(num, verifica=False):
    f = 1
    for c in range(num,0,-1):
        f*=c
    print(f'O fatorial de {num} e igual a {f}.')

    if verifica == True:
        j = 1
        for k in range(num,0,-1):
            j*=k
            print(k,end='')
            if k != 1:
                print('.',end='')
        print(f'= {f}')


num = int(input('numero: '))
fatorial(num)
verifica = input(f'Deseja ver o processo de calculo do fatorial de {num}? [s/n]: ')
if verifica == 's':
    fatorial(num, verifica=True)
'''
def fatorial(n, show=False):
    '''
    -> calcula o fatorial de um numero
    :param n: o numero a ser calculado o fatorial
    :param show: (opcional) Mostra ou nao a conta
    :return: O valor do fatorial do numero n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ',end=' ')
            else:
                print(' = ',end=' ')
        f *= c
    return f


numero = int(input('Digite um numero para obter o seu fatorial: '))
print(fatorial(numero))
calculo = input('Deseja ver o calculo?[s/n] ')
if calculo == 's':
    print(fatorial(numero,True))




#help(fatorial)