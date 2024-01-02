def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: {entrada} e um preco invalido.\033[m')
        else:
            valido = True
            return float(entrada)



