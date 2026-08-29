from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_padrao_kg = 0.4
    preco_carne_em_kg = 82.40

    def __init__(self, titulo, convidados):
        self.titulo = titulo
        self.convidados = convidados

    def analisar(self, largura = 100):
        mensagem = f"Analisando [green]{self.titulo}[/] com [blue]{self.convidados} convidados[/]\n"
        mensagem += f"Cada participante comerá {self.__class__.consumo_padrao_kg}Kg e cada Kg custa R${self.__class__.preco_carne_em_kg:.2f}\n"

        consumo_total_em_kg = self.__class__.consumo_padrao_kg * self.convidados

        mensagem += f"Recomendo [blue]comprar {consumo_total_em_kg:.3f}Kg[/] de carne\n"

        custo_total = consumo_total_em_kg * self.preco_carne_em_kg

        mensagem += f"O custo total será de [green]R${custo_total:,.2f}[/]\n"

        valor_por_pessoa = custo_total / self.convidados

        mensagem += f"Cada pessoa pagará [yellow]R${valor_por_pessoa:,.2f}[/] para participar"
        panel = Panel(mensagem, title=self.titulo, width = largura)
        print(panel)

c1 = Churrasco("Churras dos Amigos", 100)
c1.analisar()


#CONSIDERE
# Consumo padrão: 400g por pessoa
# Preço: R$82.40/kg
