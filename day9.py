# Manipulação de Strings

mensagem = "Isso aqui é um texto"

print(mensagem)

# Concatenação
primeiro_nome = "Allaph"
sobrenome = "Andersonn"

print(primeiro_nome + " " + sobrenome)

nome_completo = primeiro_nome + " " + sobrenome

print(f"Olá {nome_completo}")

# Repetir uma string

decoracao = "-" * 10

print(decoracao + "MENU" + decoracao )

# Indexação

texto = "python"

print (texto[3])

# Fatiamento - slicing

frase = "Aprender python é legal"

print(frase[9:])

print(frase[9:16]) #Da letra que eu indiquei no indice : termina -1 do indice final

# Comprimento de uma string com função LEN

print (len(frase))

# Outra maneira de formatação

cidade = "Floripa"

msg = "Eu moro em {}".format(cidade)

print(msg)

# Mudar a case da string

texto = "Programação é muito legal"

print(texto.upper()) # Letra maiúscula
print(texto.lower()) # Letra minuscula
print(texto.title()) # Toda palavra tem a sua primeira letra alterada para maiuscula

# Limpeza de espaços em brancos.

msg_com_espaco = "                 Eu quero falar com o suporte         "

print(msg_com_espaco.strip())

# Substituição

frase = "Eu gosto de voar"

nova_frase = frase.replace("voar", "programar")

print(nova_frase)

# Encontrando substring = parte de um texto
texto = "Onde está a minha chave"

posicao = texto.find("chave")

print(f"A posição é {posicao}")

posicao2 = texto.find("key")

print(f"A posição é {posicao2}") 

# Como ele não vai encontrar o texto, o retorno sempre será -1

if posicao2 == -1:
    print("Palavra não encontrada")