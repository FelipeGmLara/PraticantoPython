import random

palavras = ['marreco', 'carro', 'luz', 'arvore']
palavra = random.choice(palavras)
letras_entrada = []
chances = 5
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_entrada:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    tentativa = input("Coloque uma letra: ")
    letras_entrada.append(tentativa)
    if tentativa not in palavra:
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra not in letras_entrada:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Você acertou a palavra {palavra}")
else:
    print(f"Você perdeu a palavra era {palavra}")
