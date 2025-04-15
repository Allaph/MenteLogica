# Orientação a objetos
# Paradigma procedural: código é lido de cima para baixo
# Paradigma de orientação a objetos: Classes e objetos

# Classe -> Objeto
# Classe é o molde de objeto
# Instancia de um objeto

class Pessoa:
# Caracteristicas e ações de objetos
# Um exemplo de caracteristica é o nome de um objeto, *Na POO, caracteristicas são propriedades e atributos
# Um exemplo de ação de objeto é o ato de se apresentar, "Na POO, ações são métodos."
    def __init__(self, nome, idade):
        # Colocar o valor do argumento do meu futuro objeto
        self.nome = nome
        self.idade = idade
        # SELF é utilizado para atribuir valores aos objetos.
    def apresentacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

    def aniversario(self):
        self.idade +=1
        print(f"Fiz aniversário, agora eu tenho {self.idade} anos.")

pessoa1 = Pessoa("Joãozinho", 33)

# # Método = Função do objeto
pessoa1.apresentacao()
pessoa1.aniversario()

pessoa2 = Pessoa("Maria", 32)

pessoa2.apresentacao()

# Exercicio
# Retangulo
# Atributos: largura e altura
# Metodo: Área

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def apresentacao(self):
        print(f"A largura do retângulo é: {self.largura}cm e a altura é: {self.altura}cm.")

    def area_do_retangulo(self):
        print(f"A área do retangulo é {self.largura * self.altura}")

retangulo1 = Retangulo(5, 10)
retangulo1.apresentacao()
retangulo1.area_do_retangulo()