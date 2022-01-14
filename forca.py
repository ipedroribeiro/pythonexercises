def jogar():
    print("***************************")
    print("Bem vindo ao jogo da forca!")
    print("***************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    #enquanto(True)
    while (not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1
            print ("Ops, você errou! Faltam {} tentativas, use-as com cuidado...".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns, você ganhou!!")
    else:
        print("Infelizmente você perdeu :(")
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()