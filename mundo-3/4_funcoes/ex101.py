'''
Crie um programa que tenha uma funcao chamada voto() que vai receber como
parametro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleicoes.
'''
'''
Minha solucao

from datetime import datetime
def voto(nascimento):
    idade = ano_atual - nascimento
    if idade < 16:
        print(f'NEGADO! Com {idade} anos nao e permitido votar.')
    elif idade >= 16 and idade <18 or idade > 65:
        print(f'OPCIONAL! Com {idade} anos o voto e opcional.')
    else:
        print(f'OBRIGATORIO! Com {idade} anos o voto e obrigatorio.')




nascimento = int(input('Ano de nascimento: '))
data_atual = datetime.now()
ano_atual = data_atual.year

voto(nascimento)
'''
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NAO PODE VOTAR'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


nascimento = int(input('Em que ano voce nasceu? '))
print(voto(nascimento))