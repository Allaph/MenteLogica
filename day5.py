# Estruturas de repetição

# Repetir N vezes, onde N podemos definir ou N é uma condição

frutas = ["maçã", "banana", "laranja"]

# for item_individual in lista:
# bloco repetido N vezes

for fruta in frutas:
    print("Fruta: ", fruta)

for i in range(5):
    print("Num: ", i)

print (frutas[0])
print (frutas[2])

# While

contador = 0

while contador <5:
    print("Num while:", contador)
    contador +=1 #Se essa linha não fosse inserida, o contador não conseguiria sair do zero.

#Um loop com uma condição mal definida = loop infinito = bug

for i in range(10):
    if i == 5:
        break #Esse comando pausa o contador após atingir o if.

    print("Num for", i)

for i in range(10):
    if i == 2:
        continue #Esse comando continuará a contagem pulando o número do if anterior
    print("For in continue", i)


# Calcular a multiplicação de 1 a N

N = int (input("Digite um número: "))
multiplicacao = 0

for i in range(1, N + 1):
    resultado = N * i
    print(resultado)

# Identificar numeros pares e impares
pares = 0
impares = 0

for i in range (1, 21):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print ("Pares: ", pares)
print ("Impares: ", impares)