# Tratamento de erros e exceções
# Criar programas que precisam estar a prova de falhas
# Try, except, else, finally


# Try = Tentando fazer algo.
# Except = Tratar um erro.
# Else = Para uma condição positiva.
# Finally = Que roda sempre, independente da situação.

try: 
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo não existe")
else:
    print("Arquivo lido !")
    print(conteudo)
finally:
    print("Operação finalizada")
    # Método para liberar memória
    if 'arquivo' in locals():
        arquivo.close()
        print("Arquivo fechado")

try:
    numero = int(input("Digite um número:"))
    resultado = 100 / numero
except ValueError:
    print("Entrada inválida, tente novamente")
except ZeroDivisionError:
    print("Não é possível dividir por 0 !")
else:
    print("O resultado da divisão é: ", resultado)
finally:
    print("Operação concluída !")

# Exemplo de vários erros agrupados em um só, esse tipo de código é mais utilizado quando quem precisa saber do erro é apenas o desenvolvedor, não sendo enviado ao usuário.
try:
    numero2 = int(input("Digite um número:"))
    resultado2 = 100 / numero2
except (ValueError, ZeroDivisionError) as error:
    print("Erro:", error)
else:
    print("O resultado da divisão é: ", resultado2)
finally:
    print("Operação concluída !")
    