from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):

    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    qtd_lados = 4

    def __init__(self, lado):
        super().__init__(Quadrado.qtd_lados)
        self.lado = lado

    def perimetro(self):
        return Quadrado.qtd_lados * self.lado

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    qtd_lados = 0
    def __init__(self, raio):
        super().__init__(Circulo.qtd_lados)
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio

    def area(self):
        return pi * self.raio ** 2