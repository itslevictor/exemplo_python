def nova_operacao(historico):
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Escolha o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return
    else:
        print("Operador inválido!")
        return

    operacao = f"{num1} {operador} {num2} = {resultado}"
    historico.append(operacao)
    print(operacao)

def ver_historico(historico):
    print("\n--- Histórico ---")
    for op in historico:
        print(op)

def encerrar(historico):
    print("Encerrando a calculadora.")
    exit()

def opcao_invalida(historico):
    print("Opção inválida! Tente novamente.")

def calculadora():
    historico = []
    opcoes = {
        '1': nova_operacao,
        '2': ver_historico,
        '3': encerrar
    }

    while True:
        print("\n--- Calculadora ---")
        print("1. Nova Operação")
        print("2. Ver Histórico")
        print("3. Encerrar")
        escolha = input("Escolha uma opção: ")

        opcoes.get(escolha, opcao_invalida)(historico)

calculadora()
