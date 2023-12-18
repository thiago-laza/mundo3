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
        if sit = True and media < 5:
            resultado['situacao'] = 'Ruim'
        dicionario = resultado
    return dicionario


resp = notas(6, 5, 7, sit=True)
print(resp)