# Padrões de projeto

# Formas de programar, que vão trazer resultados benéficos para nossa aplicação

# Singleton
# Garante que uma classe tenha apenas uma instância

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Instancia Singleton criada")
        return cls._instance
    
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)

# Padrão Factory
#Define uma interface para criar objetos, mas permite que subclasses decidam qual objeto criar.

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass # Será usado para implementar nas subclasses

# Fabrica de transporte: Criar carros e barcos
# A fabrica exige um método mover.

# Subclasse de transporte
class Carro(Transporte):
    def mover(self):
        print("O carro está se movendo!")

class Barco(Transporte):
    def mover(self):
        print("O barco está se movendo!")

class fabricaTransporte:
    def criar_transporte(self, tipo):
        if tipo == "carro":
            return Carro()
        elif tipo == "barco":
            return Barco()
        else:
            raise ValueError("Tipo de transporte desconhecido")
        
fabrica = fabricaTransporte()

transp1 = fabrica.criar_transporte("carro")
transp2 = fabrica.criar_transporte("barco")

transp1.mover()
transp2.mover()