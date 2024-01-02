'''
Modifique as funcoes que foram criadas no desafio 107
para que elas aceitem um parametro a mais informando
se o valor retornado por elas vai ser ou nao formatado
pela funcao moeda(), desenvolvida no desafio 108
'''
import moeda
p = float(input('Digite o preco: R$ '))
print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')