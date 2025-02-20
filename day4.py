# condicionais = Estruturas if, else

idade = 16

# Para utilizar o if corretamente em Python, é necessário inserir um bloco onde a informação será retornada, o bloco em questão é criado com " : " onde a continuação ocorre na linha abaixo.

#If sempre vai validar se a informação é verdadeira
if idade >= 18:
    print("Você é maior de idade")

#else sempre vai ser executado quando IF não for verdadeiro
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#Meia entrada, condições: Menor que 18 anos ou estudante de rede pública ou universidade.

estuda_rede_publica = False

if idade < 18 or estuda_rede_publica:
    print("Tem direito a meia entrada")

# Classificação por nota, condições: 9 = A, 8 = B, 6 = c  /Classificação S = 10/

nota = 10

#ELIF = Junção de else + if, é uma condição intermediária entre eles.
#ANOTAÇÃO: O Elif vai retornar o valor da primeira condição verdadeira ao invés de mais de uma resposta.

if nota >= 10:
    print("Sua classificação é S")

elif nota > 9:
    print("Sua classificação é A")

elif nota > 8:
    print("Sua classificação é B")

elif nota > 6:
    print("Sua classificação é C")

else:
    print ("Melhore sua nota")

#Vendas, condições: > 1000 = 5%, >500 = 3%, 0-500 = 1%

Venda = 1005

if Venda > 1000:
    print("A porcentagem da sua comissão sobre a venda foi de 5%")

elif Venda > 505:
    print("A porcentagem da sua comissão sobre a venda foi de 3%")

elif Venda > 350:
    print("A porcentagem da sua comissão sobre a venda foi de 1%")

#Comando input vai permitir que o usuário insira uma informação, ou seja que o usuário tenha uma interação antes de seguirmos com a execução do código e respostas.
#ANOTAÇÃO: Em Python o input sempre irá retornar o que o usuário inserir como String, necessário que você converta para o que quer, utilizei FLOAT pela possibilidade do usuário não inserir um número inteiro.

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é maior que zero", numero)

else:
    print("O número é menor do que zero", numero)