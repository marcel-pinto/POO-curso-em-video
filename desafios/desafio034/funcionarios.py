from abc import ABC

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > self.salario:
            self.__salario = novo_salario
        else:
            raise ValueError("Você não pode reduzir o salário de um funcionário.")

    def calcular_bonus(self):
        pass

    def __str__(self):
        return f"{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}"

class Designer(Funcionario):
    bonus = 0.08
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario * Designer.bonus

class Gerente(Funcionario):
    bonus = 0.15
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario * Gerente.bonus

class Desenvolvedor(Funcionario):
    bonus = 0.10
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario * Desenvolvedor.bonus