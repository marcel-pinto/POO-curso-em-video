from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.console import Group
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self, largura = 30):
        total_width = largura - 4

        nome_produto = Text(f"{self.nome}", justify="center")

        preco_string  = f"R${self.preco:,.2f}"
        tamanho_string = len(preco_string)
        numero_caracteres = total_width - tamanho_string

        preco_string = (numero_caracteres // 2) * "." + preco_string + (numero_caracteres // 2) * "."
        preco_produto = Text(preco_string, justify="center")

        texto = Group(
            nome_produto, total_width * "-", preco_produto
        )
        panel = Panel(texto, title="Produto", width=largura)
        print(panel)


p1 = Produto(nome = "iPhone 17 Pro Max", preco=25_00.85)
p2 = Produto(nome = "Notebook Gamer", preco=8_000)

p1.etiqueta()
p2.etiqueta()
