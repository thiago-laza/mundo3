'''
Crie um pacote chamado utilidadeCeV que tenha dois modulos
internos chamados moeda e dado.

Transfira todas as funcoes utilizadas nos desafios 107 ate 110
para o primeiro pacote a mantenha tudo funcionando.
'''
from ex111.utilidadescev import moeda
p = float(input('Digite o preco: R$ '))
moeda.resumo(p,30,15)