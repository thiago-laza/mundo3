def metade(p):
    res = p / 2
    return res


def dobro(p):
    res = p * 2
    return res


def aumentar(p,t):
    res = p + (p * t/100)
    return res


def diminuir(p,t):
    res = p - (p * t/100)
    return res


def moeda(p):
    return f'R${p}'