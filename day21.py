# Calular número fatorial

def calcular_fatorial():
    while True:
        try:
            numero = int(input("Digite um número inteiro não negativo, para calculo de fatorial: "))
            if numero < 0:
                print("Número inválido por ser negativo")
                return
            break
        except ValueError:
            print("Entrada inválida")

    fatorial = 1

    for i in range (1, numero + 1):
        fatorial *= i

    print(f"Fatorial de {numero} é {fatorial}")

calcular_fatorial()

# Contador de palavras em um texto

def contar_palavras(texto):
    palavras = texto.strip().split()
    return len(palavras)

texto_usuario = input("Digite uma frase: ")

quantidade = contar_palavras(texto_usuario)

print(f"O texto que você forneceu tem {quantidade} palavras.")