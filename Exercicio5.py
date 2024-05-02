#Estruturas de decisão

print("Bem vindo, digite qual horário você estuda: M(Manhã),T(Tarde) ou N(Noite)")
horario = (input("Digite aqui: "))
if horario == "M":
    print("Bom dia")
elif horario == "T":
    print("Boa tarde")
elif horario == "N":
    print("Boa noite")
else:
    print("Digite um horário válido!")