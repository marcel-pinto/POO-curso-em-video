from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self, largura = 30):
        total_width = largura - 4

        conteudo = f"{self.nome.center(total_width, " ")}"
        conteudo += "-" * total_width
        preco_f = f"R${self.preco:,.2f}"
        conteudo += f"{preco_f.center(total_width, ".")}"

        etiqueta = Panel(conteudo, title="Produto", width=largura)
        print(etiqueta)


p1 = Produto(nome = "iPhone 17 Pro Max", preco=25_00.85)
p2 = Produto(nome = "Notebook Gamer", preco=8_000)

p1.etiqueta()
p2.etiqueta()
