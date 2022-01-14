#print ("Brasil ganhou cinco copas do mundo")
#print ("Brasil", "ganhou", "cinco", "copas", "do", mundo", sep="-")


#pais= "itália"
#quant=4
#print (type(pais))
#print (type(quant))
#print (pais, "ganhou", quant, "copas do mundo")


#dia= 5 
#mes= 3
#ano= 2005
#print(dia, mes, ano, sep="/")


#print ("*********************************")
#print ("Bem vindo ao jogo da adivinhação!")
#print ("*********************************")
#nmr_secreto=23
#total_de_chances=3
#rodada = 1
#for rodada in range (1, total_de_chances + 1):
#    print ("Tentativa {} de {}".format(rodada, total_de_chances))
#    chute_str =input("Digite um número entre 1 e 100:")
#    print("Você digitou", chute_str)
#    chute= int(chute_str) 
#    if (chute < 1 or chute > 100):
#        print("Você deve digitar um número entre 1 e 100!")
#        continue
#    acertou = nmr_secreto==chute
#    maior   = nmr_secreto>chute
#    menor   = nmr_secreto<chute
#    if (acertou):
#       print("Parabéns!! Você acertou!")
#       break
#    else:
#       if (menor): 
#           print ("Ah, você errou :(. O número secreto é menor que", chute) 
#       elif (maior):
#           print ("Ah, você errou :(. O número secreto é maior que", chute)
#print ("Fim do jogo")


#minha_idade = 18
#idade_namorada = 16
#if(minha_idade == idade_namorada):
#    print('temos idades iguais')
#else:
#    print('temos idades diferentes')


#numero1 = 10
#numero2 = 10
#if(numero1 == numero2):
#    print("São números iguais")


#usuario = input("Informe o usuário do sistema!")
#if(usuario == "Flávio"):
#    print("Seja bem-vindo Flávio!")
#elif(usuario == "Douglas"):
#    print("Seja bem-vindo Douglas!")
#elif(usuario == "Nico"):
#    print("Seja bem-vindo Nico")
#else:
#    print("Usuário não identificado!")


#frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']
#fruta_pedida = input('Qual é a fruta que deseja consultar ?')
#if(fruta_pedida in frutas):
#    print ('Sim, temos a fruta.')
#else:
#    print ('Não temos a fruta.')


#frutas = ['Figo', 'Banana', 'Uva', 'Melão', 'Mamão']
#fruta_buscada = 'Melancia'
#if fruta_buscada in frutas:
#    print (frutas.index(fruta_buscada))
#else:
#    print("Desculpe, a {} não está presente na lista de frutas.".format(fruta_buscada))


#instrutores = {'Nico' : 39, 'Flavio': 37,'Pedro' : 18, 'Marcos' : 30}
#print (instrutores ['Pedro'])


#total = 0
#palavra = "python rocks!"
#acabou = False
#while (not acabou):
#    acabou = (total == len(palavra))
#    total = total + 1
#print(total - 1)


#passos = 0
#while (passos<10):
#  passos += 1
#print(passos)