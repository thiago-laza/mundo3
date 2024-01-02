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