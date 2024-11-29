import random
numero_sorteado = random.randint(1, 100)
tentativas = 0 

while tentativas < 10:
    chute = int(input("digite seu chute: "))
    tentativas += 1
    if chute > numero_sorteado:
        print ("chute maior que o numero sorteado: ")
    if chute < numero_sorteado:
        print ("chute menor que o numero sorteado: ")
    else : 
        print ("voce acertou")
        break
if tentativas ==10: 
    print ("acabou seus chutes, o numero correto era", numero_sorteado)
