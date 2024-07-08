menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input('Qual o valor que você deseja depositar? R$ '))
        print('Depositando')
        saldo += deposito
        extrato += f'Foi depositado R$ {deposito:.2f} na conta. Novo Saldo: R$ {saldo:.2f} \n'
        print(f'Foi depositado R$ {deposito:.2f} na conta. Novo Saldo: R$ {saldo:.2f} \n')
    elif opcao == '2':
        saque = float(input('Digite o valor que deseja sacar? R$ '))
        print('Sacando')
        if (saque <= saldo) and (saque <= limite) and (numero_saques <= LIMITE_SAQUES):
            saldo -= saque
            numero_saques += 1
            extrato += f'Foi realizado o saque de R$ {saque:.2f} da conta. Novo Saldo: R$ {saldo:.2f} \n'
            print(f'Foi realizado o saque de R$ {saque:.2f} da conta. Novo Saldo: R$ {saldo:.2f} \n')
        else:
            print('O valor que deseja sacar não está disponível em saldo ou o limite de saque foi atingido')
    elif opcao == '3':
        print('Extrato da Conta')
        print (extrato)
    elif opcao == "0":
        break
    else:
        print('Digite uma opção válida')
    