class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if valor > 0:
            self._base = valor
        else:
            raise ValueError("O valor da base precisa ser maior que 0")

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
        else:
            raise ValueError("O valor da altura precisa ser maior que 0")
        
    @property
    def medidas(self):
        return f"Base = {self.base}\nAltura = {self.altura}\nArea = {self.area}"

    @medidas.setter
    def medidas(self, med):
        base, altura = med

        self.base = base
        self.altura = altura

    @property
    def area(self):
        self._area =  self.base * self.altura
        return self._area