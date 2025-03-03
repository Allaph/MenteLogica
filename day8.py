# Funções
# São a maneira de criar códigos que podem ser reútilizaveis

def saudacao():
    print("Olá, seja bem vindo !")
# A função precisa ser chamada

saudacao()

# Parametros = Serve para configurar a função e dar valores a elapara usar de maneira diferente a função

def saudacao_personalizada(nome):
    print(f"Olá {nome}, seja bem vindo")
# O parametro serve dentro de uma funcao como variavel

saudacao_personalizada("Matheus")
saudacao_personalizada("Pedro")
saudacao_personalizada("João")
saudacao_personalizada("Maria")

# Multiplos parametros

def apresentar_pessoa(nome, idade, profissao):
    print(f"Dados da pessoa, nome: {nome}, idade: {idade} anos, profissão: {profissao}")

apresentar_pessoa("Matheus", 33, "Programador")
apresentar_pessoa("Pedro", 22, "Influencer")
apresentar_pessoa("João", 25, "Carpinteiro")
apresentar_pessoa("Maria", 35, "Diretora executiva")

# Return: Instrução que retorna um resultado já apresentado anteriormente

def soma (a, b):
    resultado = a + b
    return resultado

soma (5, 5)

x = 10

soma_x = x + soma (5, 5)

print(soma_x)

resultado_soma = soma(1, 99)

soma_y = 10 + resultado_soma

print(soma_y)

# Criar uma função que converte Fahrenheit para Celsius

# Regras de negócio
#Criar uma função que receba a temperatura em F
#Passar pela formula de conversao (f-32) * 5/9
#Retornar o valor para o escopo global
#Imprimir o resultado

def fahrenheit_p_celsius(f):
    return (f-32) * 5/9

temp_f = 102
temp_c = fahrenheit_p_celsius(temp_f)

print(f"A temperatura {temp_f}, foi convertida para {temp_c}C")