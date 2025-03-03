# Adivinhe um número

import random

print ("Bem vindo ao jogo do 'Adivinhe um Número'")

# Repetir um código até acertar

while True:

    numero_secreto = random.randint(1, 50)

    tentativas_restantes = 5

    print("Pensei em um número entre 1 e 50")
    print("Você tem 5 tentativas para adivinhar")

    while tentativas_restantes > 0:

        # Palpite do usuário (input)
        palpite = input ("Digite o número: ")

        # Validação para checar se um usuário digitou um número
        if not palpite.isdigit():
            print("Entrada inválida! Por favor digite um número entre 1 e 50")
            continue
        
        # Converter o palpite para número inteiro
        palpite = int(palpite)

        # Ver se o número digitado está dentro do intervalo esperado
        if palpite < 1 or palpite > 50:
            print("O número deve ser entre 1 e 50")
            continue

        # Descontar tentativas
        tentativas_restantes -= 1

        # Verificar se o palpite está correto
        if palpite == numero_secreto: 
            print(f"Você acertou ! Você ainda tinha {5 - tentativas_restantes} tentativas")
            break

        elif palpite < numero_secreto:
            print("O número é maior do que esse")
        else:
            print("O número é menor do que esse")

        print(f"Tentativas restantes: {tentativas_restantes}")

    # While else, para quando as tentativas acabam
    else:
        print(f"Você perdeu, o número secreto era: {numero_secreto}")

    # Perguntar se o jogador quer tentar novamente
    jogar_novamente = input("Deseja jogar novamente ? (s/n)").lower()

    if jogar_novamente != "s":
        print("Obrigador por jogar, até a próxima...")
        break