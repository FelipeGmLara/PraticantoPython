print("Calculadora de números INTEIROS")
print("Selecione o tipo de calculo que deseja: ")
print("[1] - ADIÇÃO |[2] - SUBTRAÇÃO |[3] - MULTIPLICAÇÃO |[4] - DIVISÃO")

escolha = input(" ")
if escolha == "1":
    entrada_numero = input("Digite o primeiro número : ")
    entrada_numero2 = input("Digite o segundo número e depois aperte ENTER ")
    num1 = int(entrada_numero)
    num2 = int(entrada_numero2)
    resultado_soma = num1 + num2
    print("A conta é:", num1, "+", num2, "= ", resultado_soma)
elif escolha == "2":
    entrada_numero = input("Digite o primeiro número : ")
    entrada_numero2 = input("Digite o segundo número e depois aperte ENTER ")
    num1 = int(entrada_numero)
    num2 = int(entrada_numero2)
    resultado_subtracao = num1 - num2
    print("A conta é: ", num1, "-", num2, "= ", resultado_subtracao)
elif escolha == "3":
    entrada_numero = input("Digite o primeiro número : ")
    entrada_numero2 = input("Digite o segundo número e depois aperte ENTER ")
    num1 = int(entrada_numero)
    num2 = int(entrada_numero2)
    resultado_multiplicacao = num1 * num2
    print("A conta é: ", num1, "x", num2, "= ", resultado_multiplicacao)
elif escolha == "4":
    entrada_numero = input("Digite o primeiro número : ")
    entrada_numero2 = input("Digite o segundo número e depois aperte ENTER ")
    num1 = int(entrada_numero)
    num2 = int(entrada_numero2)
    resultado_divisao = num1 // num2
    print("A conta é: ", num1, "/", num2, "= ", resultado_divisao)
else:
    print("OPÇÃO INVALIDA")