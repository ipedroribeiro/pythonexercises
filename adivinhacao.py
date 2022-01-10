import random
#Utilizei import para importar a biblioteca random e gerar um número aleatório.

def jogar():
    print ("*********************************")
    print ("Bem vindo ao jogo da adivinhação!")
    print ("*********************************")

    nmr_secreto=random.randint(1,100)
    total_de_chances=0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("Fácil (1)  Médio (2)  Difícil (3)")
    nivel= int (input ("Defina o nível:"))

    if (nivel == 1):
        total_de_chances = 20
    elif (nivel == 2):
        total_de_chances = 10
    else:
        total_de_chances = 5

    for rodada in range (1, total_de_chances + 1):
        print ("Tentativa {} de {}".format(rodada, total_de_chances))
        chute_str =input("Digite um número entre 1 e 100:")
        print("Você digitou", chute_str)
        chute= int(chute_str)
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
    #Aqui fica a parte visual do jogo, onde o usuário digita um número e o programa verifica se o número é maior ou menor que o número secreto.
        acertou = nmr_secreto==chute
        maior   = nmr_secreto>chute
        menor   = nmr_secreto<chute

        if (acertou):
           print("Parabéns!! Você acertou e fez {} pontos!".format (pontos))
           break
        else:
           if (menor):
               print ("Ah, você errou :(. O número secreto é menor que", chute)
               if (rodada == total_de_chances):
                   print("O número secreto era {}. Você fez {} pontos no total.".format(nmr_secreto, pontos))
           elif (maior):
               print ("Ah, você errou :(. O número secreto é maior que", chute)
               if (rodada == total_de_chances):
                   print("O número secreto era {}. Você fez {} pontos no total.".format(nmr_secreto, pontos))
           pontos_perdidos = abs (nmr_secreto - chute)
           pontos = pontos - pontos_perdidos
    print ("Fim do jogo")
    #Por fim, utilizei a função if e else para definir quando o jogo acaba.

if (__name__ == "__main__"):
    jogar()