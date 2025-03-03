# Listas (array) e tuplas
# Interligadas com os loops - estruturas de repetição

carros = ["Bmw", "Fiat", "Ford"]

# Lembrando que os índices começam a contar a partir do número 0, se tem 3 itens na lista a cotagem será 0,1,2.
print(carros[0])
print (carros[2])

carros.append("VW")
# Tudo que for colocado após um objeto e tiver um . seguido de um comando, é chamado método, no caso acima 
#serve para adicionar um item a lista.

print (carros[3])

carros[0] = "Bmw Elétrica"
# Outra possibilidade de atualizar uma lista

print(carros[0])

print(carros)

carros.remove("Fiat")
# Método para remover um item da lista

print(carros)

print(len(carros))
# Len vai contar quantos itens tem na lista apontada


# Tuplas
# Cria com (1, 2, 3)
# Não pode modificar ou seja, não é possível adicionar novos itens, remover ou atualizar.

cores = ("Vermelho", "Verde", "Laranja", "Roxo")

print (cores)

print (cores[1])

for cor in cores:
    print("Cor: ", cor)

print (len(cores))

# Array/Lista: Podem ser modificados
# Tuplas: Não podem ser modificados