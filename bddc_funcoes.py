def copiar_txt(line):
    key, sep, value = line.strip().partition(" ")
    return int(key), eval(value)


def ler_codigo(cod):
    valido = False
    while not valido:
        entrada = str(input(cod)).strip()
        if not entrada.isnumeric() or len(entrada) < 4 or len(entrada) > 4:
            print('Valor Invalido!')
        else:
            valido = True
            return int(entrada)


def ler_dinheiro(pre):
    valido = False
    while not valido:
        entrada = str(input(pre)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('Valor Invalido!')
        else:
            valido = True
            return round(float(entrada), 2)


def sim_ou_nao():
    valido = False
    while not valido:
        resp = str(input()).strip()[0]
        if resp == '1':
            valido = True
            return resp
        elif resp == '2':
            valido = True
            return resp
        elif resp != '1' and resp != '2':
            print('Insira uma opção valida!')
