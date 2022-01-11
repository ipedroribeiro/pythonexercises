def jogar():
    print("***************************")
    print("Bem vindo ao jogo da forca!")
    print("***************************")

    palavra_secreta = "melancia"
    enforcou = False
    acertou = False

    #Enquanto não False (True) e não False (True).
    while(not enforcou and not acertou):

        chute = input ("Qual letra?")
        chute = chute.strip()
        index = 0

        for letra in palavra_secreta:

            if(chute.upper() == letra.upper()):
                print("Você encontrou a letra {} na posição {}".format (letra.upper(), index))
                index = index + 1

        print("jogando...")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()