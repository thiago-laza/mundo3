'''
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

def soma(*valores):
    acu = 0
    for n in valores:
        acu+=n
    print(f'A soma dos valores {valores} e igual a {acu}')


soma(2,3)
soma(2,3,4)
