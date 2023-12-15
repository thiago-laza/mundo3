'''
PARTE 1:

def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)


mensagem('sistema de alunos')
mensagem('curso em video')
mensagem('gustavo guanabara')

'''

'''
def soma(a,b):
    c = a + b
    print(c)


soma(2,3)
'''

'''
def contador(*num):
    tamanho = len(num)
    print(f'Recebi os numeros {num} que sao ao todo {tamanho} numeros.')


contador(1, 2, 3)
contador(1, 2)
contador(1, 2, 3, 4, 5, 6, 7)

'''

'''
valores = [1,2,3]
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos]*=2
        pos+=1


dobra(valores)
print(valores)
'''
'''

def soma(*valores):
    acu = 0
    for n in valores:
        acu+=n
    print(f'A soma dos valores {valores} e igual a {acu}')


soma(2,3)
soma(2,3,4)

'''
'''
PARTE 2

'''
'''
#interactive help -> usar help()
help(input)
print(input.__doc__)
'''

'''
'''
('-------------------------------------------------------------------------------------')
'''
#docstring
def contador(i,f,p):
    #''
    #Faz uma contagem e mostra na tela
    #:param i: inicio da contagem
    #:param f: fim da contagem
    #:param p: passo da contagem
    #:return: sem retorno
    '''
'''
   c = i
    while c <= f:
        print(f'{c}',end='..')
        c += p
    print('FIM')


#contador(2,10,2)
help(contador)
'''
('-------------------------------------------------------------------------------------')
'''
#parametros opcionais

def soma(a=0,b=0,c=0):
    #''
    #Faz a soma de tres valores e mostra o resultado na tela
    #:param a: o primeiro valor
    #:param b: o segundo valor
    #:param c: o terceiro valor
    #:return:
    #''
    s = a + b + c
    print(f'A soma vale {s}')


soma(3,2,5)
soma(8,4)
soma(5)
soma()
'''
('-------------------------------------------------------------------------------------')
#escopo de variaveis

'''

def teste():
    x = 8#variavel com escopo local, so vale dentro da funcao
    print(f'Na funcao teste, n vale {n}.')
    print(f'Na funcao teste, x vale {x}.')


n = 2#variavel com escopo global, vale em todo o programa
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}')->vai dar Erro, pois a variavel x so vale na funcao.
'''
'''
def funcao():
    n1 = 8
    print(f'n1 dentro da funcao vale {n1}')


funcao()
n1 = 2
print(f'n1 fora da funcao vale {n1}')
'''

'''
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro da funcao {a}')
    print(f'B dentro da funcao {b}')
    print(f'C dentro da funcao {c}')


a = 5
teste(a)
print(f'A fora da funcao {a}')
'''
('-------------------------------------------------------------------------------------')

#retornando valores

'''
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s


r1 = somar(2,3,4)
r2 = somar(3,4)
r3 = somar(3)
print(f'Meus calculos deram {r1}, {r2} e {r3}')
'''

'''
#exemplo 1
def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f*=c
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} e igual a {fatorial(n)}')
'''
#exemplo 2

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print(f'{num} e par.')
else:
    print(f'{num} nao e par.')
