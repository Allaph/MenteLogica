# Debugging
# Identificar erros no código, ou entender como o código está funcionando

# Print
def dividir(a, b):
    print(f"Dividindo {a} por {b}")
    resultado = a / b
    print(f"O resultado da divisão foi {resultado}")
    return resultado

dividir(10, 2)

# Pdb (python debugger)

import pdb

def dividir(a, b):
    
    pdb.set_trace()

    if b == 0:
        return None

    resultado = a / b
    
    return resultado

dividir(10, 2)

# Testes unitários

import unittest

def somar(a, b):
    return a + b

class Testsomar(unittest.TestCase):
    def teste_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)
    def teste_somar_negativos(self):
        self.assertEqual(somar(-1, -1), -2)
    def teste_somar_zero(self):
        self.assertEqual(somar(2, 0), 2)

if __name__ == "__main__":
    print("Iniciando testes de soma...")
    unittest.main()
