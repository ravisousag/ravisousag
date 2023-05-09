menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Informe o valor do deposito: '))

        if deposito > 0:
            saldo += deposito
            extrato.append(f'Depósito: R$ {deposito}')
            print(f'Você depositou R${deposito} e seu saldo atual é de R${saldo}\n')

        else:
            print('O valor é negativo, você só pode depositar valores positivos')

    elif opcao == 's':
        saque = float(input('Informe o valor do saque: '))

        if saque>saldo:
            print(f'Operação falhou! Você não tem saldo suficiente. Você tentou sacar R${saque} e seu saldo é de R${saldo}')

        elif saque<=saldo:
            if saque>500:
                print(f'Operação falhou! O limite máximo por saque é de R$500 e você tentou sacar R${saque}')
            elif numero_saques>=LIMITE_SAQUES:
                print('Operação falhou! Você já sacou 3 vezes')
            else:
                saldo -= saque
                extrato.append(f'Saque: R$ {saque}')
                numero_saques += 1
                print(f'Você sacou R${saque} e seu saldo atual é de R${saldo}\n')

    elif opcao == 'e':
        print('-='*20)
        print('                 EXTRATO         ')
        print(extrato)
        print('-='*20)

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')