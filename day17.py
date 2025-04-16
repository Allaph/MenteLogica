# Algoritmos para resolver problemas complexos de forma performáticas

# Recursão: Quando uma função chama ela mesmo para resolver um problema

def contar_regressivamente(n):
    if n <= 0:
        print("Fim!")
    else:
        print(n)
        contar_regressivamente(n - 1)

# Recursão é como um loop só que com funções

contar_regressivamente(10)

# Fatorial => 5 = 5 * 4 * 3 * 2 * 1

def fatorial (n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
print (fatorial(5))

# ALGORITMOS E ESTRUTURAS DE DADOS, SÃO ASSUNTOS ABORDADOS EM ENTREVISTAS DE EMPREGO

# Pesquisa binária recursiva (Divide uma lista em duas partes e procura o que foi solicitado nas duas ao mesmo tempo)
def pesquisa_binaria(lista, alvo, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1 # Indice do elemento final

    if inicio > fim:
        return -1
    
    meio = (inicio + fim) //2

    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return pesquisa_binaria(lista, alvo, meio + 1, fim) # Pesquisando na primeira metade
    else:
        return pesquisa_binaria(lista, alvo, inicio, fim - 1) # Pesquisando na segunda metade
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(f"Indice do elemento 7: {pesquisa_binaria(lista, 7)}")
print(f"Indice do elemento 15: {pesquisa_binaria(lista, 15)}")