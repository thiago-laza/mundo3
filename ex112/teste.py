'''
Dentro do pacote utilidadescev que criamos no desafio 111, temos um modulo chamado dado. Crie uma funacao
chamada leiaDinheiro() que seja capaz de funcionar com a funcao input(), mas com uma validacao de dados
para aceitar apenas valores que sejam monetario
'''
from ex112.utilidadescev import moeda, dado


p = dado.leia_dinheiro('Digite o preco: ')
moeda.resumo(p,30,15)


