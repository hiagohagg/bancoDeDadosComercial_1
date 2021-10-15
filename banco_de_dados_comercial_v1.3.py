import datetime
from bddc_funcoes import copiar_txt  # Todas as funções locais estão em outro arquivo python(bddc_funcoes.py).
from bddc_funcoes import ler_codigo
from bddc_funcoes import ler_dinheiro
from bddc_funcoes import sim_ou_nao

usuarios_do_sistema = {}  # Usuários ainda sem armazenamento de dados.
adicionar_produtos = {}
produto_adicionado = []

with open('lista_produtos.txt') as fd:  # Produtos armazenados em um arquivo de texto(lista_produtos.txt).
    produtos_da_loja = dict(copiar_txt(line) for line in fd)


class Usuario:
    """
    Registro de funcionarios e clientes com seu dados pessoais e de login.
    nome, sobrenome, sexo, idade: Caracteristicas do usuário.
    cpf, telefone, email : Informações de contato do usuário.
    senha: Senha de login no sistema.
    nivel: Classificação de permissões do usuário.
    """

    def __init__(self, nome, sobrenome, sexo, idade, cpf, telefone, email, senha, nivel):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__sexo = sexo
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.__senha = senha
        self.__nivel = nivel

    def nome_competo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def get_senha(self):
        return self.__senha

    def get_nivel(self):
        return self.__nivel


usuarios_do_sistema['cliente'] = Usuario('Cliente', 'da Loja', 'M', 20, None, None, None, '123456', 1)
usuarios_do_sistema['vendedor'] = Usuario('Vendedor', 'da Loja', 'M', 20, None, None, None, '123456', 2)
usuarios_do_sistema['gerente'] = Usuario('Gerente', 'da Loja', 'M', 20, None, None, None, '123456', 3)
# Registros de usuários genérico para testes.
# Usuários e senhas: cliente 123456; vendedor 123456; gerente 123456.

# Tela de login.
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
      '=-=-=-=-=-= BANCO DE DADOS  COMERCIAL =-=-=-=-=-=\n'
      '=-=-=-=-=-= Faça login para  começar! =-=-=-=-=-=')
valido = False
while not valido:
    usuario = str(input('USUÁRIO: ')).strip()
    if usuario in usuarios_do_sistema:
        entrada = str(input('SENHA: '))
        if usuarios_do_sistema[usuario].get_senha() == entrada:
            valido = True
        else:
            print('Senha incorreta!')
    else:
        print('Usuário não encontrado!')

    while True:
        with open('lista_produtos.txt', 'w') as lista:
            for k in produtos_da_loja.keys():  # Produtos armazenados em um arquivo de texto(lista_produtos.txt).
                lista.write(f"{k} ")
                lista.write(f"{produtos_da_loja[k]}\n")
        # Menu principal.
        print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
              f"=-=-=-=-=-= BANCO DE DADOS  COMERCIAL =-=-=-=-=-=\n"
              f"Conectado como: {usuario}\n"
              f"=-=-=-=-=-=-=- O que deseja fazer? -=-=-=-=-=-=-=")
        if usuarios_do_sistema[usuario].get_nivel() == 1:
            print('Consultar um produto........................[ 1 ]')
        if usuarios_do_sistema[usuario].get_nivel() == 2:
            print('Consultar um produto........................[ 1 ]\n'
                  'Contabilizar uma venda......................[ 2 ]')
        if usuarios_do_sistema[usuario].get_nivel() == 3:
            print('Consultar um produto........................[ 1 ]\n'
                  'Contabilizar uma venda......................[ 2 ]\n'
                  'Cadastrar um novo produto...................[ 3 ]')
        menu = int(input('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'))

        # Ferramentas do sistema nivel 1.
        if menu == 1:
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

        # Ferramentas do sistema nivel 2.
        if menu == 2 and usuarios_do_sistema[usuario].get_nivel() >= 2:
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
                        venda_atual = datetime.datetime.now()
                        with open('lista_vendas.csv', 'a') as vendas:
                            with open('nota_fiscal.txt') as nota:
                                vendas.write(f"\n{venda_atual.day}/{venda_atual.month}/{venda_atual.year},"
                                             f"{venda_atual.hour}:{venda_atual.minute},"
                                             f"R$ {valor_final},{nota.read().rsplit(' n')}")
                        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
                              '')
                        with open('nota_fiscal.txt', 'a') as nota:
                            nota.write(f"\n"
                                       f"VALOR FINAL: R$ {valor_final}\n"
                                       f"VALOR DO TROCO : R$ {valor_troco}\n")
                        with open('nota_fiscal.txt') as nota:
                            print(nota.read())
                        with open('nota_fiscal.txt', 'w') as nota:
                            nota.write('')
                        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                        break
                    elif resposta2 == '2':
                        with open('nota_fiscal.txt', 'w') as nota:
                            nota.write('')
                        break

        # Ferramentas do sistema nivel 3.
        if menu == 3 and usuarios_do_sistema[usuario].get_nivel() == 3:
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
