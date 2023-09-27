lista_contatos = [
     {"Nome": "Roberto", "Nº Telefone": "123-456-7890", "E-mail": "joao@email.com"},
       {"Nome": "Chica", "Nº Telefone": "987-654-3210", "E-mail": "maria@email.com"},
       {"Nome": "Gertrudes", "Nº Telefone": "123-456-7890", "E-mail": "joao@email.com"},
       {"Nome": "Saikomé", "Nº Telefone": "987-654-3210", "E-mail": "maria@email.com"},
       {"Nome": "ursula", "Nº Telefone": "987-654-3210", "E-mail": "ursula@email.com"},
]
contato = {}
continuar = True

#for i, contato in enumerate(lista_contatos, start=1): acrescentar no adição nos testes finais, não esquecer, substituir o id por contagem das adições de contatos.

def listar_contatos():
    print("Lista de contatos:")
    for i, contato in enumerate(lista_contatos, start=1):
        print(f"{i}. {contato['Nome']}, {contato['Nº Telefone']}, {contato['E-mail']}")

def add_contato():
        nome = input("Digite o seu nome: ")
        n_telefone = input("Digite o seu telefone: ")
        email = input("Digite o seu e-mail: ")
                
        contato = {"Nome": nome, "Nº Telefone": n_telefone, "E-mail": email}
        lista_contatos.append(contato)


def editar_contato():
    listar_contatos() 
    
    try:
        indice = int(input("Digite o número do contato que deseja editar (ou 0 para sair): ")) - 1 
        if indice == -1:
            global continuar
            continuar = False
        elif 0 <= indice < len(lista_contatos):
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo número de telefone: ")
            novo_email = input("Digite o novo e-mail: ")
            
            lista_contatos[indice]["Nome"] = novo_nome
            lista_contatos[indice]["Nº Telefone"] = novo_telefone
            lista_contatos[indice]["E-mail"] = novo_email
            print("Contato editado com sucesso!")
        else:
            print("Número de contato inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def excluir_contato(): 
    indice = int(input("digite 1 para querer excluir ou 0 para sair: ")) -1

    try:
        if indice == -1:
            return
        elif 0 <= indice < len(lista_contatos):
            listar_contatos() 
            pergunta = int(input("qual contato deseja deletar: "))
            contato_excluido = lista_contatos.pop()
            print(f"Contato excluído com sucesso!")
        else:
            print("Número invalido")
    except ValueError:
        print("Por favor, insira um número válido.")
        
        
while continuar:
    print("\nOpções:")
    print("1. Listar contatos")
    print("2. Adicionar contato")
    print("3. Editar contato")
    print("4. Excluir contato")
    print("5. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        listar_contatos()
    elif escolha == '2':
        add_contato()
    elif escolha == '3':
        editar_contato()
    elif escolha == '4':
        excluir_contato()
    elif escolha == '5':
        print("Encerrando o programa...")
        continuar = False
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

#evitar usar o break, zoa todo o código, usar uma definição e colocar == True para dar False e encerrar o processo.



        