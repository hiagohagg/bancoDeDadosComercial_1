adicionar_produtos = {}
produto_adicionado = []


def get_pair(line):
    key, sep, value = line.strip().partition(" ")
    return int(key), eval(value)


with open('lista_produtos.txt') as fd:
    produtos_da_loja = dict(get_pair(line) for line in fd)


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


while True:
    with open('lista_produtos.txt', 'w') as lista:
        for k in produtos_da_loja.keys():
            lista.write(f"{k} ")
            lista.write(f"{produtos_da_loja[k]}\n")
    menu = int(input('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
                     '=-=-=-=-=-= BANCO DE DADOS  COMERCIAL =-=-=-=-=-=\n'
                     '=-=-=-=-=-=-=- O que deseja fazer? -=-=-=-=-=-=-=\n'
                     'Cadastrar um novo produto...................[ 1 ]\n'
                     'Consultar um produto........................[ 2 ]\n'
                     'Contabilizar uma venda......................[ 3 ]\n'
                     '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'))

    if menu == 1:
        print('=-=-=-=-=-= CADASRO DE NOVOS PRODUTOS =-=-=-=-=-=')
        while True:
            adicionar_produtos.clear()
            produto_adicionado.clear()
            print('=-=-=-=-=- Insira os dados do  produto -=-=-=-=-=')
            codigo = ler_codigo('CÓDIGO: ')
            if codigo in produtos_da_loja:
                print('Produto já cadastrado!\n'
                      '=-=-=-=- Atualizar [ 1 ]  Cancelar [ 2 ] -=-=-=-=')
                resposta1 = sim_ou_nao()
                if resposta1 == '1':
                    adicionar_produtos['preco'] = ler_dinheiro('PREÇO: ')
                    adicionar_produtos['informacoes'] = str(input('INFORMAÇÕES: '))
                    produto_adicionado.append(adicionar_produtos.copy())
                    print('=-=-=-=-=-= Os dados estão  corretos? =-=-=-=-=-=\n'
                          '=-=-=-=-=- Enviar [ 1 ] Cancelar [ 2 ] -=-=-=-=-=')
                    resposta1 = sim_ou_nao()
                    if resposta1 == '1':
                        del produtos_da_loja[codigo]
                        produtos_da_loja[codigo] = produto_adicionado[:]
                        print('Atualizado com SUCESSO!')
                    elif resposta1 == '2':
                        print('Não atualizado!!')
                    print('=-=-=- Novo Cadastro [ 1 ] Finalizar [ 2 ] -=-=-=')
                    resposta2 = sim_ou_nao()
                    if resposta2 == '2':
                        break
                    else:
                        print('Produto já cadastrado!')
            if codigo not in produtos_da_loja:
                adicionar_produtos['preco'] = ler_dinheiro('PREÇO: ')
                adicionar_produtos['informacoes'] = str(input('INFORMAÇÕES: '))
                produto_adicionado.append(adicionar_produtos.copy())
                print('=-=-=-=-=-= Os dados estão  corretos? =-=-=-=-=-=\n'
                      '=-=-=-=-=- Enviar [ 1 ] Cancelar [ 2 ] -=-=-=-=-=')
                resposta1 = sim_ou_nao()
                if resposta1 == '1':
                    produtos_da_loja[codigo] = produto_adicionado[:]
                    print('Adicionado com SUCESSO!')
                elif resposta1 == '2':
                    print('Não adicionado!')
                print('=-=-=- Novo Cadastro [ 1 ] Finalizar [ 2 ] -=-=-=')
                resposta2 = sim_ou_nao()
                if resposta2 == '2':
                    break
                else:
                    print('Produto já cadastrado!')

    if menu == 2:
        print('=-=-=-=-=-=-= CONSULTA DE  PRODUTOS =-=-=-=-=-=-=')
        while True:
            codigo = ler_codigo('=-=-=-=-=- Insira o código do  produto -=-=-=-=-=\n')
            if codigo not in produtos_da_loja:
                print('Produto não cadastrado!\n'
                      '=-=-=-= Nova busca [ 1 ]  Finalizar [ 2 ] =-=-=-=')
                resposta1 = sim_ou_nao()
                if resposta1 == '2':
                    break
            else:
                print(f"PRODUTO: {produtos_da_loja[codigo][0]['informacoes']}\n"
                      f"PREÇO: R$ {produtos_da_loja[codigo][0]['preco']}\n"
                      f"=-=-=-= Nova busca [ 1 ]  Finalizar [ 2 ] =-=-=-=")
                resposta1 = sim_ou_nao()
                if resposta1 == '2':
                    break

    if menu == 3:
        print('=-=-=-=-=-= CONTABILIZAÇÃO  DE VENDAS =-=-=-=-=-=')
        valor_inicial = 0.0
        produto_comprado = {}
        while True:
            codigo = ler_codigo('=-=-=-=-=- Insira o código do  produto -=-=-=-=-=\n')
            valor_final = round(valor_inicial + produtos_da_loja[codigo][0]['preco'], 2)
            valor_inicial = valor_final
            produto_comprado['informacoes'] = produtos_da_loja[codigo][0]['informacoes']
            produto_comprado['preco'] = produtos_da_loja[codigo][0]['preco']
            with open('nota_fiscal.txt', 'a') as nota:
                nota.write(f"{produto_comprado['informacoes']} R$ {produto_comprado['preco']}\n")
            print(f"VALOR DA COMPRA: R$ {valor_final}\n"
                  f"ULTIMO PRODUTO ESCANEADO: R$ {produtos_da_loja[codigo][0]['preco']}\n"
                  f"=-=-=-=-=- Outro [ 1 ] Finalizar [ 2 ] -=-=-=-=-=")
            resposta1 = sim_ou_nao()

            if resposta1 == '2':
                print(f"VALOR FINAL DA COMPRA: R$ {valor_final}\n"
                      f"=-=-=-=- Confirmar [ 1 ]  Cancelar [ 2 ] -=-=-=-=")
                resposta2 = sim_ou_nao()
                if resposta2 == '1':
                    valor_troco = round(ler_dinheiro(f"VALOR FINAL DA COMPRA: R$ {valor_final}\n"
                                                     f"=-=-=-= Insira o valor pago pelo  cliente =-=-=-=\n")
                                        - valor_final, 2)
                    print(f"VALOR DO TROCO : R$ {valor_troco}\n"
                          f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                          f"")
                    with open('nota_fiscal.txt') as nota:
                        print(nota.read())
                    with open('nota_fiscal.txt', 'w') as nota:
                        nota.write('')
                    print(f"VALOR FINAL: R$ {valor_final}\n"
                          f"\n"
                          f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                    break
                elif resposta2 == '2':
                    break
