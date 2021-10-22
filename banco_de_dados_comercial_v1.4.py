import datetime
import pickle
from bddc_funcoes import Usuario, copiar_txt, ler_codigo, ler_dinheiro,\
                         sim_ou_nao, ler_sexo, ler_cpf, ler_nivel, ler_senha
# Todas as classes e funções locais estão em outro arquivo python(bddc_funcoes.py).

with open('lista_produtos.txt') as lp:
    produtos_da_loja = dict(copiar_txt(line) for line in lp)
# Carregar produtos armazenados em um arquivo de texto(lista_produtos.txt).

try:
    with open('lista_usuarios.pickle', 'rb') as usuarios:
        usuarios_do_sistema = dict(pickle.load(usuarios))
    # Carregar usuários armazenados em um arquivo pickle(lista_usuarios.pickle).
except:
    usuarios_do_sistema = {}
    usuarios_do_sistema['admin'] = Usuario('Adiministrador', 'do Sistema', None, None, None, None, '123456', 4)
    # Usuários possuem uma classe Usuario em outro arquivo python(bddc_funcoes.py).
    # Usuário padrão: adimin 123456.

# Tela de login.
print('\033[1m'+'\033[36m'+'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
      '=-=-=-=-=-= BANCO DE DADOS  COMERCIAL =-=-=-=-=-=\n'
      '=-=-=-=-=-= Faça login para  começar! =-=-=-=-=-='+'\033[0;0m')
valido = False
while not valido:
    usuario = str(input('\033[36m'+'USUÁRIO: ')).strip()
    if usuario not in usuarios_do_sistema:
        print('\033[31m'+'Usuário não encontrado!')
    elif usuario in usuarios_do_sistema:
        entrada = str(input('\033[36m'+'SENHA: '))
        if usuarios_do_sistema[usuario].get_senha() != entrada:
            print('\033[31m'+'Senha incorreta!')
        else:
            valido = True
            while True:
                with open('lista_produtos.txt', 'w') as produtos:
                    for k in produtos_da_loja.keys():
                        produtos.write(f"{k} ")
                        produtos.write(f"{produtos_da_loja[k]}\n")
                # Salvar produtos armazenados em um arquivo de texto(lista_produtos.txt).
                with open('lista_usuarios.pickle', 'wb') as usuarios:
                    pickle.dump(usuarios_do_sistema, usuarios)
                # Salvar usuarios em um arquivo pickle(lista_usuarios.pickle).

                # Menu principal.
                print(f'\033[1m'+'\033[36m'+"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                      f"=-=-=-=-=-= BANCO DE DADOS  COMERCIAL =-=-=-=-=-=\n"
                      f"Conectado como: {usuario}\n"
                      f"=-=-=-=-=-=-=- O que deseja fazer? -=-=-=-=-=-=-="+'\033[0;0m')
                if usuarios_do_sistema[usuario].get_nivel() == 1:
                    print('\033[1m'+'\033[36m'+'Consultar um produto........................[ 1 ]'+'\033[0;0m')
                if usuarios_do_sistema[usuario].get_nivel() == 2:
                    print('\033[1m'+'\033[36m'+'Consultar um produto........................[ 1 ]\n'
                          'Contabilizar uma venda......................[ 2 ]'+'\033[0;0m')
                if usuarios_do_sistema[usuario].get_nivel() == 3:
                    print('\033[1m'+'\033[36m'+'Consultar um produto........................[ 1 ]\n'
                          'Contabilizar uma venda......................[ 2 ]\n'
                          'Cadastrar um novo produto...................[ 3 ]\n'
                          'Consultar um usuário........................[ 4 ]'+'\033[0;0m')
                if usuarios_do_sistema[usuario].get_nivel() == 4:
                    print('\033[1m'+'\033[36m'+'Consultar um produto........................[ 1 ]\n'
                          'Contabilizar uma venda......................[ 2 ]\n'
                          'Cadastrar um novo produto...................[ 3 ]\n'
                          'Consultar um usuário........................[ 4 ]\n'
                          'Cadastrar um novo usuário...................[ 5 ]'+'\033[0;0m')
                menu = int(input('\033[1m'+'\033[36m'+'Sair........................................[ 0 ]\n'
                                 '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'+'\033[0;0m'))

                # Ferramentas do sistema nivel 1.
                if menu == 1:
                    print('\033[1m'+'\033[36m'+'=-=-=-=-=-=-= CONSULTA DE  PRODUTOS =-=-=-=-=-=-='+'\033[0;0m')
                    while True:
                        codigo = ler_codigo('\033[1m'+'\033[36m'+'=-=-=-=-=- Insira o código do  produto -=-=-=-=-=\n'
                                                                 ''+'\033[0;0m')
                        if codigo not in produtos_da_loja:
                            print('\033[31m'+'Produto não cadastrado!\n'
                                  '\033[1m'+'\033[36m'+'=-=-=-= Nova busca [ 1 ]  Finalizar [ 2 ] =-=-=-='+'\033[0;0m')
                            resposta1 = sim_ou_nao()
                            if resposta1 == '2':
                                break
                        else:
                            print('\033[1m'+'\033[36m'+f"PRODUTO: {produtos_da_loja[codigo][0]['informacoes']}\n"
                                  f"PREÇO: R$ {produtos_da_loja[codigo][0]['preco']}\n"
                                  f"=-=-=-= Nova busca [ 1 ]  Finalizar [ 2 ] =-=-=-="+'\033[0;0m')
                            resposta1 = sim_ou_nao()
                            if resposta1 == '2':
                                break

                if menu == 0:
                    valido = False
                    print('\033[1m'+'\033[36m'+'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
                          '=-=-=-=-=-= BANCO DE DADOS  COMERCIAL =-=-=-=-=-=\n'
                          '=-=-=-=-=-= Faça login para  começar! =-=-=-=-=-='+'\033[0;0m')
                    break

                # Ferramentas do sistema nivel 2.
                if menu == 2 and usuarios_do_sistema[usuario].get_nivel() >= 2:
                    print('\033[1m'+'\033[36m'+'=-=-=-=-=-= CONTABILIZAÇÃO  DE VENDAS =-=-=-=-=-='+'\033[0;0m')
                    valor_inicial = 0.0
                    produto_comprado = {}
                    while True:
                        codigo = ler_codigo('\033[1m'+'\033[36m'+'=-=-=-=-=- Insira o código do  produto -=-=-=-=-=\n'
                                                                 ''+'\033[0;0m')
                        valor_final = round(valor_inicial + produtos_da_loja[codigo][0]['preco'], 2)
                        valor_inicial = valor_final
                        produto_comprado['informacoes'] = produtos_da_loja[codigo][0]['informacoes']
                        produto_comprado['preco'] = produtos_da_loja[codigo][0]['preco']
                        with open('nota_fiscal.txt', 'a') as nota:
                            nota.write(f"{produto_comprado['informacoes']} R$ {produto_comprado['preco']}\n")
                        print('\033[1m'+'\033[36m'+f"VALOR DA COMPRA: R$ {valor_final}\n"
                              f"ULTIMO PRODUTO ESCANEADO: R$ {produtos_da_loja[codigo][0]['preco']}\n"
                              f"=-=-=-=-=- Outro [ 1 ] Finalizar [ 2 ] -=-=-=-=-="+'\033[0;0m')
                        resposta1 = sim_ou_nao()
                        if resposta1 == '2':
                            print('\033[1m'+'\033[36m'+f"VALOR FINAL DA COMPRA: R$ {valor_final}\n"
                                  f"=-=-=-=- Confirmar [ 1 ]  Cancelar [ 2 ] -=-=-=-="+'\033[0;0m')
                            resposta2 = sim_ou_nao()
                            if resposta2 == '1':
                                valor_troco = round(ler_dinheiro('\033[1m'+'\033[36m'+f"VALOR FINAL DA "
                                                                                      f"COMPRA: R$ {valor_final}\n"
                                                                 f"=-=-=-= Insira o valor pago pelo  cliente =-=-=-=\n"
                                                                                      f""+'\033[0;0m')
                                                    - valor_final, 2)
                                venda_atual = datetime.datetime.now()
                                with open('lista_vendas.csv', 'a') as vendas:
                                    with open('nota_fiscal.txt') as nota:
                                        vendas.write(f"\n{usuario},{venda_atual.day},{venda_atual.month},"
                                                     f"{venda_atual.year},{venda_atual.hour}:{venda_atual.minute},"
                                                     f"R$ {valor_final},{nota.read().rsplit(' n')}")
                                print('\033[32m'+'Venda finalizada!\n'
                                      '\033[1m'+'\033[36m'+'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
                                                           '\n'+'\033[0;0m'
                                                           '                   NOTA FISCAL                   \n')
                                with open('nota_fiscal.txt', 'a') as nota:
                                    nota.write(f"\n"
                                               f"VALOR FINAL: R$ {valor_final}\n"
                                               f"VALOR DO TROCO : R$ {valor_troco}\n"
                                               f"{venda_atual.day}/{venda_atual.month}/{venda_atual.year} "
                                               f"{venda_atual.hour}:{venda_atual.minute}\n")
                                with open('nota_fiscal.txt') as nota:
                                    print(nota.read())
                                with open('nota_fiscal.txt', 'w') as nota:
                                    nota.write('')
                                print('\033[1m'+'\033[36m'+'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
                                                           ''+'\033[0;0m')
                                break
                            elif resposta2 == '2':
                                with open('nota_fiscal.txt', 'w') as nota:
                                    nota.write('')
                                break

                # Ferramentas do sistema nivel 3.
                if menu == 3 and usuarios_do_sistema[usuario].get_nivel() >= 3:
                    adicionar_produtos = {}
                    produto_adicionado = []
                    print('\033[1m'+'\033[36m'+'=-=-=-=-=-= CADASRO DE NOVOS PRODUTOS =-=-=-=-=-='+'\033[0;0m')
                    while True:
                        adicionar_produtos.clear()
                        produto_adicionado.clear()
                        print('\033[1m'+'\033[36m'+'=-=-=-=-=- Insira os dados do  produto -=-=-=-=-='+'\033[0;0m')
                        codigo = ler_codigo('\033[36m'+'CÓDIGO: ')
                        if codigo in produtos_da_loja:
                            print('\033[31m'+'Produto já cadastrado!\n'
                                  '\033[1m'+'\033[36m'+'=-=-=-=- Atualizar [ 1 ]  Cancelar [ 2 ] -=-=-=-='+'\033[0;0m')
                            resposta1 = sim_ou_nao()
                            if resposta1 == '1':
                                adicionar_produtos['preco'] = ler_dinheiro('\033[36m'+'PREÇO: ')
                                adicionar_produtos['informacoes'] = str(input('\033[36m'+'INFORMAÇÕES: '))
                                produto_adicionado.append(adicionar_produtos.copy())
                                print('\033[1m'+'\033[36m'+'=-=-=-=-=-= Os dados estão  corretos? =-=-=-=-=-=\n'
                                      '=-=-=-=-=- Enviar [ 1 ] Cancelar [ 2 ] -=-=-=-=-='+'\033[0;0m')
                                resposta1 = sim_ou_nao()
                                if resposta1 == '1':
                                    del produtos_da_loja[codigo]
                                    produtos_da_loja[codigo] = produto_adicionado[:]
                                    print('\033[32m'+'Atualizado com SUCESSO!')
                                elif resposta1 == '2':
                                    print('\033[31m'+'Não atualizado!')
                                print('\033[1m'+'\033[36m'+'=-=-=- Novo Cadastro [ 1 ] Finalizar [ 2 ] -=-=-='
                                                           ''+'\033[0;0m')
                                resposta2 = sim_ou_nao()
                                if resposta2 == '2':
                                    break
                                else:
                                    print('\033[31m'+'Produto já cadastrado!')
                        if codigo not in produtos_da_loja:
                            adicionar_produtos['preco'] = ler_dinheiro('\033[36m'+'PREÇO: ')
                            adicionar_produtos['informacoes'] = str(input('\033[36m'+'INFORMAÇÕES: '))
                            produto_adicionado.append(adicionar_produtos.copy())
                            print('\033[1m'+'\033[36m'+'=-=-=-=-=-= Os dados estão  corretos? =-=-=-=-=-=\n'
                                  '=-=-=-=-=- Enviar [ 1 ] Cancelar [ 2 ] -=-=-=-=-='+'\033[0;0m')
                            resposta1 = sim_ou_nao()
                            if resposta1 == '1':
                                produtos_da_loja[codigo] = produto_adicionado[:]
                                print('\033[32m'+'Adicionado com SUCESSO!')
                            elif resposta1 == '2':
                                print('\033[31m'+'Não adicionado!')
                            print('\033[1m'+'\033[36m'+'=-=-=- Novo Cadastro [ 1 ] Finalizar [ 2 ] -=-=-='+'\033[0;0m')
                            resposta2 = sim_ou_nao()
                            if resposta2 == '2':
                                break
                            else:
                                print('\033[31m'+'Produto já cadastrado!')

                if menu == 4 and usuarios_do_sistema[usuario].get_nivel() >= 3:
                    print('\033[1m'+'\033[36m'+'=-=-=-=-=-=-=- CONSULTA DE USUÁRIO -=-=-=-=-=-=-='+'\033[0;0m')
                    while True:
                        digitar_usuario = str(input('\033[1m'+'\033[36m'+''
                                                    '=-=-=-=-=-= Insira o nome de  usuário =-=-=-=-=-=\n'+'\033[0;0m'))\
                                                    .strip().lower()
                        if digitar_usuario not in usuarios_do_sistema:
                            print('\033[31m'+'Usuário não cadastrado!\n'
                                  '\033[1m'+'\033[36m'+'=-=-=-= Nova busca [ 1 ]  Finalizar [ 2 ] =-=-=-='+'\033[0;0m')
                            resposta1 = sim_ou_nao()
                            if resposta1 == '2':
                                break
                        else:
                            print('\033[1m'+'\033[36m'+f""
                                  f"NOME COMPLETO: {usuarios_do_sistema[digitar_usuario].nome_competo()}\n"
                                  f"SEXO: {usuarios_do_sistema[digitar_usuario].get_sexo()}\n"
                                  f"CPF: {usuarios_do_sistema[digitar_usuario].get_cpf()}\n"
                                  f"TELEFONE: {usuarios_do_sistema[digitar_usuario].get_telefone()}\n"
                                  f"EMAIL: {usuarios_do_sistema[digitar_usuario].get_email()}\n"
                                  f"=-=-=-= Nova busca [ 1 ]  Finalizar [ 2 ] =-=-=-="+'\033[0;0m')
                            resposta1 = sim_ou_nao()
                            if resposta1 == '2':
                                break

                # Ferramentas do sistema nivel 4.
                if menu == 5 and usuarios_do_sistema[usuario].get_nivel() == 4:
                    print('\033[1m'+'\033[36m'+'=-=-=-=-=-= CADASRO DE NOVOS USUÁRIOS =-=-=-=-=-='+'\033[0;0m')
                    while True:
                        digitar_usuario = str(input('\033[36m'+'NOME DE USUÁRIO: ')).strip().lower()
                        if digitar_usuario in usuarios_do_sistema or digitar_usuario == '':
                            print('\033[31m'+'Nome de usuário indisponivel!')
                        else:
                            digitar_senha = ler_senha('\033[36m'+'SENHA DO USUÁRIO: ')
                            digitar_nome = str(input('\033[36m'+'NOME: ')).strip().capitalize()
                            digitar_sobrenome = str(input('\033[36m'+'SOBRENOME: ')).strip().capitalize()
                            digitar_sexo = ler_sexo('\033[36m'+'SEXO [ M / F ]: ')
                            digitar_nivel = ler_nivel('\033[36m'+'NIVEL DO USUÁRIO [ 1 / 2 / 3 / 4 ]: ')
                            digitar_cpf = ler_cpf('\033[36m'+'CPF: ')
                            digitar_telefone = str(input('\033[36m'+'TELEFONE: ')).strip()
                            digitar_email = str(input('\033[36m'+'EMAIL: ')).strip()
                            print('\033[1m'+'\033[36m'+'=-=-=-=-=-= Os dados estão  corretos? =-=-=-=-=-=\n'
                                  '=-=-=-=-=- Enviar [ 1 ] Cancelar [ 2 ] -=-=-=-=-='+'\033[0;0m')
                            resposta1 = sim_ou_nao()
                            if resposta1 == '1':
                                usuarios_do_sistema[digitar_usuario] = Usuario(digitar_nome, digitar_sobrenome,
                                                                               digitar_sexo, digitar_cpf,
                                                                               digitar_telefone, digitar_email,
                                                                               digitar_senha, digitar_nivel,
                                                                               )
                                print('\033[32m'+'Adicionado com SUCESSO!')
                            if resposta1 == '2':
                                print('\033[31m'+'Não adicionado!')
                        print('\033[1m'+'\033[36m'+'=-=-=- Novo Cadastro [ 1 ] Finalizar [ 2 ] -=-=-='+'\033[0;0m')
                        resposta1 = sim_ou_nao()
                        if resposta1 == '2':
                            break
