import random

print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")

num_secreto = random.randint(1, 100)
tentativas = 0
limite_tentativas = 3
chute = False

print("De 0 a 100, qual número estou pensando? ")

#print(num_secreto) - para saber qual número é antes de tentar.

while not chute and tentativas < limite_tentativas:
    chutou = int(input(" "))
    tentativas += 1

    if chutou == num_secreto:
        chute = True
        print("ACERTOU!")
    elif chutou < num_secreto:
        print("TENTE UM NUMÉRO MAIOR")
    else:
        print("TENTE UM NÚMERO MENOR")
if not chute:
    print(f"3 TENTATIVAS ERRADAS, VOCÊ PERDEU!\nO NÚMERO QUE PENSEI ERA {num_secreto}")