MIN_TEMPERATURA = 16
MAX_TEMPERATURA = 30

class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,valor):
        if valor % 0.5 != 0:
            raise ValueError(f"Temperatura de {valor} °C é inválida!")
        if valor < MIN_TEMPERATURA:
            self.__temperatura = MIN_TEMPERATURA
        elif valor > MAX_TEMPERATURA:
            self.__temperatura = MAX_TEMPERATURA
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"{self.temperatura} °C"