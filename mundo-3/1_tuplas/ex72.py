'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte

Seu programa deverá ler um número pelo teclado
(entre 0 e 20)
e mostrá-lo por extenso'''

numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dozoito',
           'dezenove','vinte')

valor_numero = int(input('Digite um numero para ver seu nome por extenso: '))

while valor_numero < 0 or valor_numero > 20:
    valor_numero = int(input('Valor invalido, digite um valora nao negativo e menor ou igual a vinte: '))

print(f'O numero {valor_numero} por extenso e {numeros[valor_numero]}')

