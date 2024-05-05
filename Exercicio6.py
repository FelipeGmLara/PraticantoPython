print("Seja bem vindo a sorveteria!")
print("Digite o número correspondente ao sabor de sorvete que deseja: ")
print(" [1] - Chocolate |R$ 2,50 \n [2] - Morango |R$ 2,50 \n [3] - Flocos |R$ 2,50")

escolha = input()
sabor = " "
preco_sorvete = 0
if escolha == "1":
    sabor = "chocolate"
    preco_sorvete = 2.50
elif escolha == "2":
    sabor = "morango"
    preco_sorvete = 2.50
elif escolha == "3":
    preco_sorvete = 2.50
    sabor = "flocos"
else:
    print("Opção de sabor inválida")

print("Agora escolha o tamanho do pote: \n [1] - Pequeno |R$ 3\n [2] - Médio |R$ 4 \n [3] - Grande |R$ 5")

escolha_tamanho = input()
tamanho = " "
preco_tamanho = 0
if escolha_tamanho == "1":
    tamanho = "pequeno"
    preco_tamanho = 3
elif escolha_tamanho == "2":
    tamanho = "médio"
    preco_tamanho = 4
elif escolha_tamanho == "3":
    preco_tamanho = 5
    tamanho = "grande"
else:
    print("Opção de sabor inválida")
preco_total = preco_sorvete + preco_tamanho
print("Revisão do pedido\nVocê escolheu o sabor", sabor, "e o tamanho", tamanho, "\nO total do seu pedido é de: R$ ",
      preco_total)
