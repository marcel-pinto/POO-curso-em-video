from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_padrao_kg = 0.4
    preco_carne_em_kg = 82.40

    def __init__(self, titulo, convidados):
        self.titulo = titulo
        self.convidados = convidados

    def __str__(self):
        return f"Esse é {self.titulo} com {self.convidados} pessoas participando"

    def calcular_qtd_carne(self) -> float:
        return self.convidados * Churrasco.consumo_padrao_kg

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_carne_em_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.convidados

    def analisar(self, largura = 100):
        mensagem = f"Analisando [green]{self.titulo}[/] com [blue]{self.convidados} convidados[/]\n"
        mensagem += f"Cada participante comerá {self.__class__.consumo_padrao_kg}Kg e cada Kg custa R${self.__class__.preco_carne_em_kg:.2f}\n"
        mensagem += f"Recomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne\n"
        mensagem += f"O custo total será de [green]R${self.calcular_custo_total():,.2f}[/]\n"
        mensagem += f"Cada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar"
        panel = Panel(mensagem, title=self.titulo, width = largura)
        print(panel)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

c2 = Churrasco("Festa do fim de ano", 80)
c2.analisar()
#CONSIDERE
# Consumo padrão: 400g por pessoa
# Preço: R$82.40/kg
