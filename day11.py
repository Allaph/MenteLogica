# Dicionarios em python são como objetos em outras linguagens
# Dicionarios {}

aluno = {
    "nome": "Matheus",
    "Profissão": "Programador",
    "Idade": 33
}

print(aluno["nome"])

print(f"O nome dele é {aluno["nome"]} e sua profissão é {aluno["Profissão"]}")

aluno["nota"] = 15
aluno["Profissão"] = "Engenheiro"

print(aluno)

# Remoção

del aluno["Profissão"]

print(aluno)

# Conjunto (set)
lista = [1,2,2,2,3,4,4,5,6,7,7]

lista_unica = set(lista)

print(lista)

print(lista_unica)

lista_unica.add(8)
lista_unica.add(6)

lista_unica.remove(2)

print(lista_unica)

# União dos conjuntos

lista_b = {1,3,5}

uniao = lista_unica.union(lista_b)

print(uniao)

# Interseção

intersecao = lista_unica.intersection(lista_b)

print(intersecao)

# Diferença

diferenca = lista_unica.difference(lista_b)

print(diferenca)

# Exercicios

# Criar uma funcao que vai adicionar a nota da prova A a um aluno

def adicionar_nota(aluno):
    aluno["prova_a"] = int(input("Digite a nota A:"))

aluno_teste = {
    "nome": "João"
}

adicionar_nota(aluno_teste)

print (aluno_teste)

# Verificar as palavras unicas de uma frase (set)

frase = input("Digite uma frase: ")

palavras = frase.split()

print(palavras)

palavras_unicas = set(palavras)

print(palavras_unicas)