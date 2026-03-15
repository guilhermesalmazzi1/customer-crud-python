import json
def funcao_cadastro():
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
        cliente = {}
        cliente["nome"] = input("\nDigite o nome do cliente: ")
        novo_cpf = input("Digite o cpf do cliente: ")
        cpf_existe = False
        for c in dados:
            if c["cpf"] == novo_cpf:
                cpf_existe = True
                break
        if cpf_existe:
            print("CPF já cadastrado.")
        else:
            cliente["cpf"] = novo_cpf
            cliente["telefone"] = input("Digite o telefone do cliente: ")
            cliente["email"] = input("Digite o e-mail do cliente: ")

            dados.append(cliente)
            with open("dados.json", "w") as arquivo:
                json.dump(dados, arquivo, indent=4)

def funcao_mostrar():
        with open("dados.json", 'r') as arquivo:
            dados=json.load(arquivo)
        print("\nClientes já cadastrados:")
        for cliente in dados:
            print(cliente)

def funcao_busca():
        cpf_busca=input("Digite o cpf: ")
        with open("dados.json", 'r') as arquivo:
            dados=json.load(arquivo)
        encontrado = False
        for cliente in dados:
            if cliente["cpf"] == cpf_busca:
                print("\nCliente encontrado:")
                print(f"Nome: {cliente['nome']}")
                print(f"CPF: {cliente['cpf']}")
                print(f"Telefone: {cliente['telefone']}")
                print(f"Email: {cliente['email']}")
                encontrado = True
                break
        if not encontrado:
            print("Cliente não encontrado.")

def funcao_alter():
        cpf_alterar=input("\nDigite o cpf de quem quer fazer alteracao: ")
        with open("dados.json", 'r') as arquivo:
            dados=json.load(arquivo)
        encontrado= False
        for cliente in dados:
            if cliente["cpf"]==cpf_alterar:
                print("Cliete encontrado: ")
                print(cliente)
                campo=input("Qual campo deseja alterar? (nome, telefone, email) ")
                if campo in cliente:
                    novo_valor=input("Digite o novo valor: ")
                    cliente[campo]=novo_valor
                    print("Dados atualizados.")
                else:
                    print("Campo inválido.")
                encontrado= True
                break
        if not encontrado:
            print("Cliente não encontrado.")
        with open("dados.json","w") as arquivo:
            json.dump(dados, arquivo, indent=4)

def funcao_apagar():
        cpf_apagar=input("\nDigite o cpf de quem quer fazer apagar da lista: ")
        with open("dados.json", 'r') as arquivo:
            dados=json.load(arquivo)
        encontrado= False
        for cliente in dados:
            if cliente["cpf"]==cpf_apagar:
                print("Cliete encontrado: ")
                print(cliente)
                resp=input("Deseja mesmo apagar esse cliente? (sim/nao) ")
                if resp=="sim":
                    dados.remove(cliente)
                    print("Cliente removido com sucesso.")
                else:
                    print("Operação cancelada.")
                encontrado= True
                break
        if not encontrado:
            print("Cliente não encontrado.")
        with open("dados.json","w") as arquivo:
            json.dump(dados, arquivo, indent=4)