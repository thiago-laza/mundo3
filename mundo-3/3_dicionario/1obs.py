'''
filmes = {
    'titulo':'star wars',
    'ano':1877,
    'diretor':'george lucas'
}

print(filmes.values())
print(filmes.keys())
print(filmes.items())


for k,v in filmes.items():
    print(f'o {k} e {v}')
'''

'''
locadora = [{'filme':'star wars','ano':1977,'diretor':'george lucas'},{'filme':'matrix','ano':1998,'diretor':'wawa'}]

print(locadora[0]['filme'])
print(locadora[1]['diretor'])
'''
'''
pessoas = {'nome':'thiago','idade':40}

for k,v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['idade']

for k,v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome']='fabiana'

for k,v in pessoas.items():
    print(f'{k} = {v}')

pessoas['peso']=69

for k,v in pessoas.items():
    print(f'{k} = {v}')
'''

'''
brasil = []
estado1 = {'uf':'rio de janeiro','sigla':'rj'}
estado2 = {'uf':'sao paulo','sigla':'sp'}

print(estado1)
print(estado2)

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['sigla'])
print(brasil[1]['uf'])
'''

estado = dict()
brasil = list()

for c in range(3):
    estado['uf']=input('Unidade federativa: ')
    estado['sigla']=input('Sigla: ')
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()