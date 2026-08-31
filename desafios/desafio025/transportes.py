from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia, frete):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete():
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia, Moto.fator)

    def calc_frete(self):
        valor = self.distancia * self.frete
        return f"R${valor:,.2f}"

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia, Caminhao.fator)

    def calc_frete(self):
        if self.distancia > 50:
            valor = self.distancia * self.frete
            return f"R${valor:,.2f}"
        else:
            return "Raio mínimo de 50Km"
class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia, Drone.fator)

    def calc_frete(self):
        if self.distancia <= 10.:
            valor = self.distancia * self.frete
            return f"R${valor:,.2f}"
        else:
            return "Raio máximo de 10Km"