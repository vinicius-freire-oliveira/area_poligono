# Definição da classe Retangulo
class Retangulo:

    # Método construtor para inicializar os atributos do retângulo
    def __init__(self, x, y):
        # Atributos privados __x e __y representam as dimensões do retângulo
        self.__x = x
        self.__y = y
        # Atributo privado __area calcula e armazena a área do retângulo
        self.__area = x * y

    # Método público para obter a área do retângulo
    def obter_area(self):
        return self.__area

# Cria uma instância da classe Retangulo com as dimensões 7 e 6
r = Retangulo(7, 6)

# Tenta definir um novo valor para o atributo 'area' da instância 'r'
r.area = 7

# Imprime a área do retângulo usando o método obter_area
print(r.obter_area())
