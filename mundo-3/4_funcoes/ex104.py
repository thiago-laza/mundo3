'''
Crie um programa que tenha a funcao leiaint() que vai funcionar de forma
semelhante a funcao input(), so que fazendo a validacao para aceitar apenas
um valor numerico.

Porgrama:

n = leiaint('Digite um numero: ')
print('voce acabou de digitar o numero {n}')

obs: caso nao seja um numero inteiro, mensagem de erro e pedir novamente para
o usuario digitar.
'''
def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro, digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor



n = leia_int('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')