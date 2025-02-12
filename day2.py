# Variáveis
idade = 25
nome = 'Matheus'
altura = 1.68

#Tipos de dados
#int, float, textos = strings, bool = true ou false

cidade = 'Sao Paulo'

esta_logado = True

print(nome)

nome = 2

print (nome)

#Verificar o tipo de dado
print(type(nome)) #int = Integer
print(type(cidade)) #str = String
print(type(esta_logado))#bool = Boolean
print(type(altura))#bool = Float

print(5 + 1.2)
print(10 * 2)
print(5 / 10)
print(50 - 25)

#Concatenação -> União dos textos
#Unir com o simbolo +

nomeUsuario = 'Joao'

frase = 'Olá ' + nomeUsuario + " tudo bem ?"

print (frase)

#Comparações
maior = 15 > 2

print(maior)

menor = 5 < 12
menor2 = 5 < 2

print(menor)
print(menor2)

print(5 == 5)
print("teste" == "teste")
print("Matheus" == "matheus")

print(15 != 2)

#Revisão de alguns conceitos

num = 10

num2 = num

print(num2)

num = 12

print(num)

print('numero: ', num)

operacao_matematica = num + 12

print (operacao_matematica)

print (12 > 5)
comp = 12 > 5

print (comp)

print((12 + 1) * 2)

num3 = 10

num4 = num + num3

print (num4)

#Exercicios

#Exercicio 01 Declarando Variáveis

nome_completo = (input("Digite o seu nome: "))
idadetotal = (input('Digite a sua idade:' ))
alturatotal = (input('Digite sua altura: '))
estudante = (input('Você é um(a) estudante ?: '))

#Exercicio 02 Exibindo informações
print("Nome:", nome_completo)
print("Idade:", idadetotal)
print("Altura:", alturatotal)
print("Estudante:", estudante)

#Exercicio 03 Operações Simples
ano_nascimento = int (idadetotal) - 2023

print(ano_nascimento)

maior_de_idade = int (idadetotal) >= 18

print("Maior de idade:", maior_de_idade)


#Exercicio 04 Manipulação de Strings
frase = "Olá, meu nome é " + nome_completo + " e eu tenho " + str(idadetotal) + " anos"
print(frase)

#Ecercicio 05 Calculadora Simples
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)


