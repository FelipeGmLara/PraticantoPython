print("Calculadora de números INTEIROS")
print("Selecione o tipo de calculo que deseja: ")
print("[1] - ADIÇÃO |[2] - SUBTRAÇÃO |[3] - MULTIPLICAÇÃO |[4] - DIVISÃO")

escolha = input(" ")


def adicao():
    entrada = int(input("Digite aqui o primeiro valor: "))
    entrada2 = int(input("Digite aqui o segundo valor: "))
    print("Resultado da sua soma é:", entrada + entrada2)


def subtracao():
    entrada = int(input("Digite aqui o primeiro valor: "))
    entrada2 = int(input("Digite aqui o segundo valor: "))
    print("Resultado da sua subtração é:", entrada - entrada2)


def multiplicacao():
    entrada = int(input("Digite aqui o primeiro valor: "))
    entrada2 = int(input("Digite aqui o segundo valor: "))
    print("Resultado da sua multiplicação é:", entrada * entrada2)


def divisao():
    entrada = int(input("Digite aqui o primeiro valor: "))
    entrada2 = int(input("Digite aqui o segundo valor: "))
    if entrada == 0:
        print("Erro: Divisão por ZERO.")
    else:
        print("Resultado da sua divisão é:", entrada / entrada2)


if escolha == "1":
    print("HORA DE SOMAR")
    adicao()
elif escolha == "2":
    print("HORA DE SUBTRAIR")
    subtracao()
elif escolha == "3":
    print("HORA DE MULTIPLICAR")
    multiplicacao()
elif escolha == "4":
    print("HORA DE DIVIDIR")
    divisao()
else:
    print("OPÇÃO INVALIDA")