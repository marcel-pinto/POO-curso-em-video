MIN_TEMPERATURA = 16
MAX_TEMPERATURA = 30

class Termostato:
    def __init__(self):
        self.__temperatura = 24
        self.ftemperatura = f"{self.__temperatura} °C"

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,valor):
        if not isinstance(valor, int):
            rounded_valor = round(valor, ndigits=1)
            decimal = int((rounded_valor - int(rounded_valor)) * 10)
            if decimal != 5:
                raise ValueError(f"Temperatura de {valor} °C é inválida!")

        if valor < MIN_TEMPERATURA:
            self.__temperatura = MIN_TEMPERATURA
        elif valor > MAX_TEMPERATURA:
            self.__temperatura = MAX_TEMPERATURA
        else:
            self.__temperatura = valor
        
        self.ftemperatura = f"{self.__temperatura} °C"