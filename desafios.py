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

desafio 2

def votar():
    votos_candidato_a = 0
    votos_candidato_b = 0
    votos_candidato_c = 0
    votos_candidato_d = 0
    votos_brancos = 0
    votos_nulos = 0
    total_votantes = 0

    while True:
        try:
            voto = int(input("Digite seu voto (1-Candidato A, 2-Candidato B, 3-Candidato C, 4-Candidato D, 5-Voto em Branco): "))
        except ValueError:
            print("Entrada inválida! Digite um número entre 1 e 5.")
            continue

        if voto == 1:
            votos_candidato_a += 1
        elif voto == 2:
            votos_candidato_b += 1
        elif voto == 3:
