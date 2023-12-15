'''
faca um programa que tenha uma funcao chamada
escreva(), que receba um texto qualquer como
parametro e mostre uma mensagem com tamanho
adaptavel.

PROGRAMA
escreva('ola,mundo!')
saida:
--------
ola mundo
--------
-------------------------
thiago cavalcanti azevedo
-------------------------
'''
def escreva(msg):
    tam = len(msg)+4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)


msg = input('Escreva uma mensagem: ')
escreva(msg)