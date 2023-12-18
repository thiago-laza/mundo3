'''
Faca um programa que tenha uma funcao notas() que pode receber varias notas de alunos
e retornar um dicionario com as seguintes informacoes:

- quantidade de notas
- a maior nota
- a menor nota
- a media da turma
- a situacao (opcional)

adicione tambem as docstring da funcao.

Programa:
resp = notas(...,sit=False(nao coloca situacao) sit=True(coloca situacao))
saida:{'total': 4,'maior':10,'menor':5.5,'media':7.8}
saidacom
obs: colocar help
'''
def notas(*n,sit=False):
    '''
    -> Funcao que recebe notas, identifica maior, menor e a media. Situacao e opicional.
    :param n: numero de notas
    :param sit: opcional a situacao do estudante.
    :return: um dicionario.
    '''
    cont = 0
    acu = 0
    resultado = {}
    maior_nota = menor_nota = None
    for c in range(len(n)):
        acu+=n[c]
        cont+=1
        media = acu/cont
        resultado['total'] = cont
        if maior_nota is None or n[c] > maior_nota:
            maior_nota = n[c]
            resultado['maior'] = maior_nota
        if menor_nota is None or n[c] < menor_nota:
            menor_nota = n[c]
            resultado['menor'] = menor_nota
        resultado['media'] = media
        if sit:
            if resultado['media'] < 5:
                resultado['situacao'] = 'Ruim'
            elif 5 <= resultado['media'] < 7:
                resultado['situacao'] = 'Regular'
            elif 7 <= resultado['media'] < 8:
                resultado['situacao'] = 'Bom'
            elif 8 <= resultado['media'] <= 10:
                resultado['situacao'] = 'Excelente'
        dicionario = resultado
    return dicionario


resp = notas(8, 8, 10, sit=True)
print(resp)
help(notas)