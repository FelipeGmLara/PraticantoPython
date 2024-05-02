#Estruturas de decisão

print("Vamos ver qual número é maior")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número que digitou é maior que o segundo número digitado.")
elif numero1 == numero2:
    print("Números iguais.")
else:
    print("O segundo número digitado é maior que o primeiro número digitado.")