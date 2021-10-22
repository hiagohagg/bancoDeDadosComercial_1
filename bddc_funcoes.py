class Usuario:
    """
    Registro de funcionarios e clientes com seu dados pessoais e de login.
    nome, sobrenome, sexo, idade: Caracteristicas do usuário.
    cpf, telefone, email : Informações de contato do usuário.
    senha: Senha de login no sistema.
    nivel: Classificação de permissões do usuário.
    """

    def __init__(self, nome, sobrenome, sexo, cpf, telefone, email, senha, nivel):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.__senha = senha
        self.__nivel = nivel

    def nome_competo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def get_sexo(self):
        return self.__sexo

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    def get_nivel(self):
        return self.__nivel


def copiar_txt(line):
    key, sep, value = line.strip().partition(" ")
    return int(key), eval(value)


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
            print('\033[31m'+'Insira uma opção valida!')


def ler_codigo(cod):
    valido = False
    while not valido:
        entrada = str(input(cod)).strip()
        if not entrada.isnumeric() or len(entrada) < 4 or len(entrada) > 4:
            print('\033[31m'+'Valor invalido!')
        else:
            valido = True
            return int(entrada)


def ler_dinheiro(din):
    valido = False
    while not valido:
        entrada = str(input(din)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[31m'+'Valor invalido!')
        else:
            valido = True
            return round(float(entrada), 2)


def ler_sexo(sex):
    valido = False
    while not valido:
        entrada = str(input(sex)).strip().upper()
        if entrada == 'M':
            valido = True
            return entrada
        elif entrada == 'F':
            valido = True
            return entrada
        elif entrada != 'M' or entrada != 'F':
            print('\033[31m'+'Insira uma opção valida!')


def ler_cpf(cpf):
    valido = False
    while not valido:
        entrada = str(input(cpf)).strip()
        if not entrada.isnumeric() or len(entrada) < 11 or len(entrada) > 11:
            print('\033[31m'+'Valor invalido!')
        else:
            valido = True
            return int(entrada)


def ler_nivel(niv):
    valido = False
    while not valido:
        resp = str(input(niv)).strip()[0]
        if resp == '1' or resp == '2' or resp == '3' or resp == '4':
            valido = True
            return int(resp)
        else:
            print('\033[31m'+'Insira uma opção valida!')


def ler_senha(sen):
    valido = False
    while not valido:
        entrada = str(input(sen)).strip()
        if len(entrada) < 6:
            print('\033[31m'+'Valor invalido!')
        else:
            valido = True
            return entrada
