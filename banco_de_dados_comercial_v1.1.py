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
            print('Insira uma opção  valida!')


while True:
    menu = int(input('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
                     '=-=-=-=-=-= BANCO DE DADOS  COMERCIAL =-=-=-=-=-=\n'
                     '=-=-=-=-=-=-=- O que deseja fazer? -=-=-=-=-=-=-=\n'
                     'Cadastrar um novo produto...................[ 1 ]\n'
                     'Consultar um produto........................[ 2 ]\n'
                     'Contabilizar uma compra.....................[ 3 ]\n'
                     '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'))

    if menu == 1:
        while True:
            adicionar_produtos.clear()
            produto_adicionado.clear()
            print('=-=-=-=-=- Insira os dados do  produto -=-=-=-=-=')
            codigo = ler_codigo('CÓDIGO: ')
            adicionar_produtos['preço'] = ler_dinheiro('PREÇO: ')
            adicionar_produtos['informaçoes'] = str(input('INFORMAÇÕES: '))
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

    if menu == 2:
        while True:
            pesq = ler_codigo('=-=-=-=-=- Insira o código do  produto -=-=-=-=-=')
            print(f"PRODUTO: {produtos_da_loja[pesq][0]['informaçoes']}\n"
                  f"PREÇO: R$ {produtos_da_loja[pesq][0]['preço']}\n"
                  f"=-=-=-= Nova busca [ 1 ]  Finalizar [ 2 ] =-=-=-=")
            resposta1 = sim_ou_nao()
            if resposta1 == '2':
                break

    if menu == 3:
        valor_inicial = 0.0
        produto_comprado = {}
        while True:
            pesq = ler_codigo('=-=-=-=-=- Insira o código do  produto -=-=-=-=-=\n')
            valor_final = round(valor_inicial + produtos_da_loja[pesq][0]['preço'], 2)
            valor_inicial = valor_final
            produto_comprado['informaçoes'] = produtos_da_loja[pesq][0]['informaçoes']
            produto_comprado['preço'] = produtos_da_loja[pesq][0]['preço']
            with open('nota_fiscal.txt', 'a') as nota:
                nota.write(f"{produto_comprado['informaçoes']} R$ {produto_comprado['preço']}\n")
            print(f"VALOR DA COMPRA: R$ {valor_final}\n"
                  f"ULTIMO PRODUTO ESCANEADO: R$ {produtos_da_loja[pesq][0]['preço']}\n"
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
