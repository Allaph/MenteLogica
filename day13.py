# Como trabalhar com arquivos em Python

# Uma forma de ler todo o arquivo
with open ('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Como ler o arquivo linha por linha
with open ('dados.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())
        break

# Escrever e se o arquivo não existir, o comando write também cria o arquivo

with open('saida.txt', 'w') as arquivo:
    arquivo.write("Nova linha \n")
    arquivo.write("Nova linha 2 \n")

# Da forma acima, o conteúdo sempre será reescrito.

# Com o código abaixo, é possível adicionar novas informações no arquivo
with open('saida.txt', 'a') as arquivo:
    arquivo.write("Nova linha 3")

# R = Read - Ler
# W = Write - Escrever
# A = Append - Adicionar

# CSV = Comma Separated Values - Arquivos com multiplos dados como, planilhas de excell.
import csv

with open("contatos.csv", "w", newline='') as arquivo_csv:
    # Cabeçalho (colunas)
    # Dados
    # Dados
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Nome', 'Profissao', 'Idade'])
    escritor.writerow(['Pedro', 'Pedreiro', 29])
    escritor.writerow(['Marcelo', 'Marceneiro', 31])
    escritor.writerow(['Kepler', 'Coach', 18])

# JSON = Javascript Object Notation (APIs)

import json

dados = {
    'nome': 'Pedro',
    'Idade': 29,
    'Profissao': 'Pedreiro'
}

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=2)