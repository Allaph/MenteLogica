#Operadores Aritméticos

a = 5
b = 2

print(a + b)
print(a * b)
print(a / b)

# ** (Realizar exponenciação)
# // (Realizar divisão de número inteiro)
#  % (Verificar o resto da divisão)

print(a // b)

#Operadores de comparação
x = 10
y = 5

print(x > 5)
# > Maior que
print(x < 5)
# < Menor que
print(x != 5)
# Valor é diferente
print(5 >= 5)
# Maior ou igual a outro
print(5 <= 1)
# Menor ou igual a outro

#Operadores lógicos
# AND, OR e NOT

# Serve para unir comparações

idade = 20
possui_carteira = True

pode_dirigir = (idade >= 18) and possui_carteira == True
print (pode_dirigir)

#AND só é verdadeiro quando ambas operacores resultam em TRUE
#OR só é verdadeiro quando uma das operações é TRUE

eh_estudante = False
idade = 60

# Um = é atribuição
# Dois == é comparação
meia_entrada = eh_estudante == True or idade >= 60

print(meia_entrada)

#NOT vai inverter um booleano

chovendo = True
nao_chovendo = not True

print('Chovendo', chovendo)
print('Não chovendo', nao_chovendo)

#Revisão
# Análise se o aluno passou de ano, para passar precisa ter nota > 7 e frequencia > 80%

nota = 8
frequencia = 60

passou_de_ano = (nota > 7) and frequencia >= 80
print('Passou de ano: ', passou_de_ano)

#Divisão de conta
#Total da conta = 123.85

conta = 123.85
pessoas = 3
parte_de_cada_um = conta / pessoas
print('Cada um deve pagar: ', parte_de_cada_um)
 
