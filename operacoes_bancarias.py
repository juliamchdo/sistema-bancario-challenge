menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[o] Sair
"""

saldo = 0
valor_limite_saque = 500
extrato = ""
numero_saques_feitos = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Valor depósito: "))

        if valor_deposito <= 0:
            print("Digite um valor válido")
        else:
            saldo += valor_deposito
            extrato += f"""
            ----------------------------
            Depósito de R${float(valor_deposito)} 
            ----------------------------
            """
            print("Depósito realizado com sucesso!")

    if opcao == "s":
        if numero_saques_feitos == LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários (3).")
        else:
            valor_saque = float(input("Valor a sacar: "))
            if valor_saque > saldo:
                print("Saldo insuficiente")
            elif valor_saque > valor_limite_saque:
                print(f"O valor máximo permitido de saques é de {valor_limite_saque}")
            else:
                saldo -= valor_saque
                numero_saques_feitos += 1
                extrato += f"""
            ----------------------------
            Saque de R${float(valor_saque)} 
            ----------------------------
                """
                print("Saque realizado com sucesso!")

    if opcao == "e":
        print(extrato + f"\n Saldo de {saldo}")

    if opcao == "o": 
        break
    else:
        print("Opção inválida")