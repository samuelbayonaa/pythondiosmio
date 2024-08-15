import math

class Figura:
    def calcular_area(self):
        pass  
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

if __name__ == "__main__":
    circulo = Circulo(5)
    cuadrado = Cuadrado(4)
    triangulo = Triangulo(6, 3)

    print(f"Área del círculo: {circulo.calcular_area()}")
    print(f"Área del cuadrado: {cuadrado.calcular_area()}")
    print(f"Área del triángulo: {triangulo.calcular_area()}")
