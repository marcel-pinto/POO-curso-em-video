import locale
from typing import List
locale.setlocale(locale.LC_ALL, 'pt_br.UTF-8')

class Carrinho:
    def __init__(self):
        self.produtos: List[Produto] = []

    @property
    def total(self):
        if len(self.produtos) > 0 :
            return sum(produto.preco for produto in self.produtos)
        return 0

    def __add__(self, other):
        if isinstance(other, Produto):
            self.produtos.append(other)

        if isinstance(other, Carrinho):
            self.produtos += other.produtos
            
        return self


    def __str__(self):
        mensagem = "-" * 30 + "\n"
        if len(self.produtos) > 0:
            for produto in self.produtos:
                mensagem += f"{produto.__str__()}\n"
        mensagem += "-" * 30 + "\n"
        mensagem += f"Total: {locale.currency(self.total, grouping=True)}"
        return mensagem

class Produto:
    def __init__(self, nome: str = "", preco:float = 0.):
        self.nome = nome
        self.preco = preco


    def __str__(self):
        return f"{self.nome} ({locale.currency(self.preco, grouping=True)})"