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
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))


escreva('thiago')
escreva('thiago cavalcanti azevedo')