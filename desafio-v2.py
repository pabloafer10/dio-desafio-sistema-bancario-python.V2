import textwrap

# Menu de opções de operações bancárias
def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCadastrar Usuário
    [5]\tCriar Contas
    [6]\tListar Contas
    [0]\tSair
    =======================================
    Por favor, selecione a opção desejada (0-6): 
    =>
    """
    return input(textwrap.dedent(menu))

# Função Depositos somente em valores positivos, todos depósitos deve ser armazenados em uma variavel e exibir na operação de extrato. Em caso de valor inválido deve ser exibido a mensagem: "Valor inválido, tente novamente." Para V2 A função depósito deve receber os argumentos apenas por posição (positional only), os argumentos devem ser: conta, numero da conta, valor e extrato, onde o retorno deve ter conta e extrato. Em caso de conta não localizada deve ser exibido a mensagem: "Conta não localizada, retorne ao menu e tente novamente.", para conta localizada com sucesso deve ser exibido a mensagem: "Depósito realizado com sucesso!". e para valores inválidos deve ser exibido a mensagem: "Valor inválido, retorne ao menu e tente novamente."
def depositar(contas, numero_conta, valor, extrato):
    if numero_conta not in contas:
        print("\n@@@ Conta não localizada, retorne ao menu e tente novamente. @@@")
        return contas, extrato

    if valor > 0:
        contas[numero_conta]["saldo"] += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Valor inválido, retorne ao menu e tente novamente.  @@@")

    return contas, extrato

# Função Sacar Limite diário de 3 saques. Caso o limite diário de saque seja maior do que permitido, deve ser exibido a mensagem: "Limite de saques diário excedido! Por favor, tente novamente." O Valor máximo de saque é de R$ 500,00 por saque. Caso o saldo seja insuficiente, deve ser exibido a mensagem: "Saldo insuficiente! Por favor, tente novamente." Caso o valor do saque seja inválido, deve ser exibido a mensagem: "Valor informado inválido, tente novamente." Todos os saques devem ser armazenados e exibidos na consulta de extrato. Para V2 A função saque deve receber os argumentos apenas por nome (keyword only). os argumentos devem ser: saldo, valor, extrato, limite, numero_saques, limite_saques, onde o retorno deve ter conta e extrato. Em caso de conta não localizada deve ser exibido a mensagem: "Conta não localizada, retorne ao menu e tente novamente.", para conta localizada com sucesso deve ser exibido a mensagem: "Saque realizado com sucesso!". para saldo insuficiente deve ser exibido a mensagem: "Saldo insuficiente, retorne ao menu e tente novamente.", para valor do saque excedendo o limite deve ser exibido a mensagem: "Valor do saque excede o limite, retorne ao menu e tente novamente." e para limite de saque diário deve ser exibido a mensagem: "Limite de saque diário excedido, retorne ao menu e tente novamente." e para valor inválido deve ser exibido a mensagem: "Valor inválido, retorne ao menu e tente novamente."
def sacar(contas, numero_conta, valor, extrato, limite, limite_saques):
    if numero_conta not in contas:
        print("\n@@@ Conta não localizada, retorne ao menu e tente novamente.  @@@")
        return contas, extrato

    saldo = contas[numero_conta]["saldo"]
    numero_saques = contas[numero_conta]["numero_saques"]

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Saldo insuficiente, retorne ao menu e tente novamente. @@@")
    elif excedeu_limite:
        print("\n@@@ Valor do saque excede o limite, retorne ao menu e tente novamente. @@@")
    elif excedeu_saques:
        print("\n@@@ Limite de saques diário excedido, retorne ao menu e tente novamente. @@@")
    elif valor > 0:
        contas[numero_conta]["saldo"] -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        contas[numero_conta]["numero_saques"] += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Valor inválido, retorne ao menu e tente novamente. @@@")

    return contas, extrato

# Função Extrato, deve exibir o extrato da conta corrente com todos os depósitos e saques realizados, No final, exibe o saldo disponível no formato: R$ xxx.xx." Para V2 A função extrato deve receber os argumentos por posição e nome (positional only e keyword only), os argumentos devem ser: saldo e extratos. 
def exibir_extrato(contas, numero_conta, extrato):
    if numero_conta not in contas:
        print("\n@@@ Conta não localizada, retorne ao menu e tente novamente. @@@")
        return

    saldo = contas[numero_conta]["saldo"]
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

# Função para criar um usuário com nome, data de nascimento, CPF e endereço, implemantada na V2 soment, em caso de conta não localizada deve ser exibido a mensagem: "Conta não localizada, retorne ao menu e tente novamente.", para usuário ja cadastrado deve ser exibida a mensagem "Usuário já cadastrado, retorne ao menu e tente novamente." em caso de usuário criado, deve ser exibida a mensagem "Usuário criado com sucesso!".
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Usuário já cadastrado, retorne ao menu e tente novamente. @@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

# Função para filtrar usuário por CPF, implemantada na V2 somente.
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para criar uma conta com agência, número da conta e usuário, implemantada na V2 somente, em caso de usuário não localizado deve ser exibido a mensagem: "Usuário não localizado, retorne ao menu e tente novamente." em caso de conta criada, deve ser exibida a mensagem "Conta criada com sucesso!".
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0, "numero_saques": 0}
    
    print("\n@@@ Usuário não localizado, retorne ao menu e tente novamente. @@@")

# Função para listar todas as contas cadastradas, implemantada na V2 somente. deve exibir a agência, número da conta, titular e saldo.
def listar_contas(contas):
    for conta in contas:
        linha = f"""\   
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            Saldo:\t\tR$ {conta.get('saldo', 0):.2f}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função main com as variáveis de controle do desafio
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    limite = 500.00
    extrato = ""
    usuarios = []
    contas = {}

# Laço de repetição para exibir o menu de opções
    while True:
        opcao = menu()

# Menu de opções de operações bancárias inputadas pelo usuário ma opção 1 - Depositar 
        if opcao == "1":
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta not in contas:
                print("\n@@@ Conta não localizada, retorne ao menu e tente novamente. @@@")
                continue

            valor = float(input("Informe o valor do depósito: "))
            contas, extrato = depositar(contas, numero_conta, valor, extrato)
# Menu de opções de operações bancárias inputadas pelo usuário ma opção 2 - Sacar 
        elif opcao == "2":
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta not in contas:
                print("\n@@@ Conta não localizada, retorne ao menu e tente novamente. @@@")
                continue

            valor = float(input("Informe o valor do saque: "))
            contas, extrato = sacar(contas, numero_conta, valor, extrato, limite, LIMITE_SAQUES)
# Menu de opções de operações bancárias inputadas pelo usuário ma opção 3 - Extrato 
        elif opcao == "3":
            numero_conta = int(input("Informe o número da conta: "))
            exibir_extrato(contas, numero_conta, extrato)
# Menu de opções de operações bancárias inputadas pelo usuário ma opção 4 - Criar usuários 
        elif opcao == "4":
            criar_usuario(usuarios)
# Menu de opções de operações bancárias inputadas pelo usuário ma opção 5 - Criar Contas
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas[numero_conta] = conta
# Menu de opções de operações bancárias inputadas pelo usuário ma opção 6 - Listar Contas criadas
        elif opcao == "6":
            listar_contas(contas.values())
# Menu de opções de operações bancárias inputadas pelo usuário ma opção 0 - Sair
        elif opcao == "0":
            break
# Menu de opções de operações bancárias inputadas pelo usuário ma opção != 0-6 - inválida 
        else:
            print("\n@@@ Opção inválida, retorne ao menu e tente novamente. @@@")

main()