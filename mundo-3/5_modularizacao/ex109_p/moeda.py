def metade(p, formato=False):
    res = p /2
    if formato is not False:
        return res
    else:
        return moeda(res)


def dobro(p, formato=False):
    res = p * 2
    if formato is not False:
        return res
    else:
        return moeda(res)


def aumentar(p, formato=False):
    res = p * 1.1
    if formato is not False:
        return res
    else:
        return moeda(res)


def diminuir(p, formato=False):
    res = p * 0.87
    if formato is not False:
        return res
    else:
        return moeda(res)


def moeda(p):
    return f'R${p:>2.2f}'.replace('.',',')