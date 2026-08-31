from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    sal_min = 1612.00
    inss = 0.075

    def __init__(self, nome):
        self.nome = nome
        self.salario_bruto = 0.
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        mensagem = f"O salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R${self.salario:,.2f}[/] e corresponde a [yellow]{self.salario/Funcionario.sal_min:.1f} salários mínimos[/]."
        panel = Panel(mensagem,title="Análise de Salário", width=40)
        print(panel)


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calcular_salario(self):
        self.salario_bruto = self.valor_hora * self.horas_trab
        self.salario = self.salario_bruto * (1 - Horista.inss)


class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calcular_salario(self):
        self.salario = self.salario_bruto * (1 - Mensalista.inss)