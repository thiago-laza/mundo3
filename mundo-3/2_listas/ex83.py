'''
crie um programa onde o usuario digite uma expressao qualquer
que use parenteses. seu aplicativo devera analisar se a espressao
esta com os parenteses abertos e fechados na ordem correta.
'''
'''
obs: nao resolvido
'''

expr = input('Digite a expressao: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao e valida.')
else:
    print('Sua expressao esta errada.')

