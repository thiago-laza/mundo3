'''
Crie uma tupla preenchida com os 20 primeiros colocados do campeonato
brasileiro de futebol, na orem de colocacao. Depois mostre:
a)apenas os 5 primeiros colocados
b)os ultimos 4 colocados na tabela
c)uma lista com os times em ordem alfabetica
d)em que posicao na tabela esta o time bahia.
'''

times = ('Palmeiras','Flamengo','Bota Fogo','Atletico MG','Gremio','Bragantino','Fluminense','Atletico PR'
         'Cuiaba','Sao Paulo','Internacional','Fortaleza','Cruzeiro','Corinthians','Santos','Vasco','Bahia',
         'Goias','Coritiba','America MG')

print(90*'-')
print(f'Os cinco primeiros colocados sao: {times[:5]}')
print(90*'-')
print(f'Os quatro ultimos colocados sao: {times[15:]}')
print(90*'-')
print(f'Os times em ordem alfabetica sao: {sorted(times)}')
print(90*'-')
print(f'O Bahia esta na posicao: {times.index("Bahia")}')