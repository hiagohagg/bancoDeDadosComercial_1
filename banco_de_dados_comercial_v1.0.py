adicionar_produtos = {}
produto_adicionado = []
produtos_da_loja = {}


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
            return float(entrada)


while True:
    menu = int(input('=-=-=-=-=-=-=- O que deseja fazer? -=-=-=-=-=-=-=\n'
                     'Cadastrar um novo produto...................[ 1 ]\n'
                     'Consultar um produto........................[ 2 ]\n'
                     'Contabilizar uma compra.....................[ 3 ]\n'
                     '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='))

    if menu == 1:
        while True:
            adicionar_produtos.clear()
            produto_adicionado.clear()
            print('=-=-=-=-=- Insira os dados do  produto -=-=-=-=-=')
            codigo = ler_codigo('CÓDIGO: ')
            adicionar_produtos['preço'] = ler_dinheiro('PREÇO: ')
            adicionar_produtos['informaçoes'] = str(input('INFORMAÇÕES: '))
            produto_adicionado.append(adicionar_produtos.copy())
            resposta1 = str(input('=-=-=-=-=-= Os dados estão  corretos? =-=-=-=-=-=\n'
                                  '=-=-=-=-=- Enviar [ 1 ] Cancelar [ 2 ] -=-=-=-=-='))[0]
            if resposta1 == '1':
                produtos_da_loja[codigo] = produto_adicionado[:]
                print('Adicionado com SUCESSO!')
            elif resposta1 == '2':
                print('Não adicionado!')
            elif resposta1 != '1' and resposta1 != '2':
                while resposta1 != '1' and resposta1 != '2':
                    resposta1 = str(input('Insira uma opção  valida!\n'
                                          '=-=-=-=-=- Enviar [ 1 ] Cancelar [ 2 ] -=-=-=-=-='))[0]
                    if resposta1 == '1':
                        produtos_da_loja[codigo] = produto_adicionado[:]
                        print('Adicionado com SUCESSO!')
                    elif resposta1 == '2':
                        print('Não adicionado!')

            resposta2 = str(input('=-=-=- Novo Cadastro [ 1 ] Finalizar [ 2 ] -=-=-='))[0]
            if resposta2 != '1' and resposta2 != '2':
                while resposta2 != '1' and resposta2 != '2':
                    resposta2 = str(input('Insira uma opção  valida!\n'
                                          '=-=-=- Novo Cadastro [ 1 ] Finalizar [ 2 ] -=-=-='))[0]
                    if resposta2 == '2':
                        break
            elif resposta2 == '2':
                break

    if menu == 2:
        while True:
            pesq = ler_codigo('=-=-=-=-=- Insira o código do  produto -=-=-=-=-=')
            resposta1 = str(input(f"PRODUTO: {produtos_da_loja[pesq][0]['informaçoes']}\n"
                                  f"PREÇO: R$ {produtos_da_loja[pesq][0]['preço']}\n"
                                  f"=-=-=-= Nova busca [ 1 ]  Finalizar [ 2 ] =-=-=-="))[0]
            if resposta1 == '2':
                break
            elif resposta1 != '1' and resposta1 != '2':
                while resposta1 != '1' and resposta1 != '2':
                    resposta1 = str(input('Insira uma opção  valida!\n'
                                          '=-=-=-= Nova busca [ 1 ]  Finalizar [ 2 ] =-=-=-='))[0]
                    if resposta1 == '2':
                        break

    if menu == 3:
        valor_inicial = 0.0
        while True:
            pesq = ler_codigo('=-=-=-=-=- Insira o código do  produto -=-=-=-=-=')
            valor_final = valor_inicial + produtos_da_loja[pesq][0]['preço']
            valor_inicial = valor_final
            resposta1 = str(input(f"VALOR DA COMPRA: R$ {valor_final}\n"
                                  f"ULTIMO PRODUTO ESCANEADO: R$ {produtos_da_loja[pesq][0]['preço']}\n"
                                  f"=-=-=-=-=- Outro [ 1 ] Finalizar [ 2 ] -=-=-=-=-="))
            if resposta1 == '2':
                resposta2 = str(input(f"VALOR FINAL DA COMPRA: R$ {valor_final}\n"
                                      f"=-=-=-=- Confirmar [ 1 ]  Cancelar [ 2 ] -=-=-=-="))
                if resposta2 == '1':
                    valor_troco = ler_dinheiro('=-=-=-= Insira o valor pago pelo  cliente =-=-=-=') - valor_final
                    print(f"VALOR DO TROCO : R$ {valor_troco}\n"
                          f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                    break
                elif resposta2 != '2':
                    while resposta2 != '2':
                        resposta2 = str(input('Insira uma opção  valida!\n'
                                              '=-=-=-=- Confirmar [ 1 ]  Cancelar [ 2 ] -=-=-=-='))
                        if resposta2 == '1':
                            valor_troco = ler_dinheiro(
                                '=-=-=-= Insira o valor pago pelo  cliente =-=-=-=') - valor_final
                            print(f"VALOR DO TROCO : R$ {valor_troco}\n"
                                  f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                            break
                elif resposta2 == '2':
                    break
            elif resposta1 != '1' and resposta1 != '2':
                while resposta1 != '1' and resposta1 != '2':
                    resposta1 = str(input('Insira uma opção  valida!\n'
                                          '=-=-=-=-=- Outro [ 1 ] Finalizar [ 2 ] -=-=-=-=-='))
                    if resposta1 == '2':
                        resposta2 = str(input(f"VALOR FINAL DA COMPRA: R$ {valor_final}\n"
                                              f"=-=-=-=- Confirmar [ 1 ]  Cancelar [ 2 ] -=-=-=-="))
                        if resposta2 == '1':
                            valor_troco = ler_dinheiro(
                                '=-=-=-= Insira o valor pago pelo  cliente =-=-=-=') - valor_final
                            print(f"VALOR DO TROCO : R$ {valor_troco}\n"
                                  f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                        elif resposta2 != '2':
                            while resposta2 != '2':
                                resposta2 = str(input('Insira uma opção  valida!\n'
                                                      '=-=-=-=- Confirmar [ 1 ]  Cancelar [ 2 ] -=-=-=-='))
                                if resposta2 == '1':
                                    valor_troco = ler_dinheiro(
                                        '=-=-=-= Insira o valor pago pelo  cliente =-=-=-=') - valor_final
                                    print(f"VALOR DO TROCO : R$ {valor_troco}\n"
                                          f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                                    break
                                elif resposta2 == '2':
                                    break
                        elif resposta2 == '2':
                            break
