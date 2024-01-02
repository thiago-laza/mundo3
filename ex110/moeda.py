def metade(p=0, t=0):
    res = p / 2
    return moeda(res)


def dobro(p=0):
    res = p * 2
    return moeda(res)


def aumentar(p=0, t=0):
    res = p + (p * t/100)
    return moeda(res)


def diminuir(p=0, t=0):
    res = p - (p * t/100)
    return moeda(res)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:>3.2f}'.replace('.', ',')


def resumo(p=0, t1=10, t2=5):
    print(30*'-')
    print('RESUMO DO VALOR'.center(30))
    print(30 * '-')
    print(f'Preco analisado: \t{moeda(p)}')
    print(f'Dobro do preco: \t{dobro(p)}')
    print(f'Metade do preco: \t{metade(p)}')
    print(f'{t1}% de aumento: \t{aumentar(p,t1)}')
    print(f'{t2}% de reducao: \t{diminuir(p,t2)}')
    print(30 * '-')
