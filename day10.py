# Módulos
# Pacotes que podem ou não estar no python
# Se estiver, basta utilizar o "import"
# Se não estiver, basta instalar com gerenciador de depencias PIP
# OBS: É sempre importante utilizar módulos e pacotes pois são otimizados e ganhamos tempo!!

import math

numero = 16
raiz_quadrada = math.sqrt(numero)

print(f"A raíz quadrade de {numero} é {raiz_quadrada} !")

from math import pi

print(f"O valor de pi é: {pi} !")

# Importar toda a biblioteca utilizar import
# Importar parcialmente, utilize = from x(biblioteca) import y,z,t(o que quer importar dela)

import math as m # alias, math = m  (Atribuir uma letra para reduzir e facilitar o nome da biblioteca)

print(f"O cosseno de 0 é: {m.cos(0)}")

# Geralmente os imports ficam no topo do arquivo

import random

dado = random.randint(1, 6)

print(f"O número é {dado}")

# Datas = date.time

from datetime import datetime

agora = datetime.now()

print(agora)

# Sistema operacional = OS
import os

arquivos = os.listdir ('.')
# . diretorio (pasta) atual

print(f"Os arquivos desta pasta são: {arquivos}")

import sys

print(f"A versão do python é: {sys.version}")