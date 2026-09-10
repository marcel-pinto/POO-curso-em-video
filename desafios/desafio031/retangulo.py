class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor da base deve ser um número.")
        
        if valor > 0:
            self._base = valor
        else:
            raise ValueError("O valor da base precisa ser maior que 0")

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor da altura deve ser um número.")

        if valor > 0:
            self._altura = valor
        else:
            raise ValueError("O valor da altura precisa ser maior que 0")
        
    @property
    def medidas(self):
        return f"Base = {self.base}\nAltura = {self.altura}\nArea = {self.area}"

    @medidas.setter
    def medidas(self, valores: tuple):
        if not isinstance(valores, tuple):
            raise TypeError("As medidas devem ser informadas dentro de uma tupla")
        if len(valores) != 2:
            raise SyntaxError("Medidas recebe (base, altura).")
        base, altura = valores

        self.base = base
        self.altura = altura

    @property
    def area(self):
        self._area =  self.base * self.altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError("Área não pode ser configurada desse jeito")