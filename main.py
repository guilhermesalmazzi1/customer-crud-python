import json
import modulo1
print("Cadastro de clientes")
while True:
    opcao=input("\nDigite o que quer fazer: cadastro, busca, alteracao, apagar, mostrar tudo ou encerrar: ")
    if opcao=="encerrar":
        print("Sessão encerrada.")
        break
    
    elif opcao == "cadastro":
        modulo1.funcao_cadastro()

    elif opcao=="mostrar tudo":
        modulo1.funcao_mostrar()

    elif opcao=="busca":
        modulo1.funcao_busca()

    elif opcao=="alteracao":
        modulo1.funcao_alter()

    elif opcao=="apagar":
        modulo1.funcao_apagar()

    else:
        print("\nEssa opção não existe, tente novamente.")
