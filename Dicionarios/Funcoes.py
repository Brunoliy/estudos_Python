def perguntar():
    return input("<I> - Para Inserir um usuário\n"+
                  "<P> - Para Pesquisar um usuário\n"+
                  "<E> - Para Excluir um usuário\n"+
                  "<L> - Para listar usuários\n"+
                 "O que deseja realizar?\n").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ")] = [input("Digite o nome: ").upper(),
                                            input("Digite a senha: "),
                                            input("Digite a última data de acessso: "),
                                            input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome: " + lista[0])
        print("Último acesso em: " + lista[2])
        print("Última estação: " + lista[3])

def excluir(dicionario, senha, chave):
    lista = dicionario.get(chave)
    if lista != None and senha==lista[1]:
        del dicionario[chave]
        print("Objeto excluido!")
    else:
        print("Acesso negado!")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto"
              "\nLogin", chave,
              "\nDados:", valor)


def salvar (dicionario):
    with open ("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))