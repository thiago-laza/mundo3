'''
Crie um programa que tenha uma tupla com varias palavras
(nao usar acentos). Depois disso, voce deve mostrar, para
cada palavra, quais sao as suas vogais.
'''

palavras = ('Thiago','Fabiana','Luana','Vinicius','Pink','Ozzy','Schoidger','Brisa')
vogais = ('a','e','i','o','u')


for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    