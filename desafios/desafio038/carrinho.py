from typing import List

class Produto:
    def __init__(self, nome: str = "", preco:float = 0.):
        self.nome = nome
        self.preco = preco


    def __str__(self):
        return f"{self.nome} ({formata_dinheiro(self.preco)})"


class Carrinho:
    def __init__(self, produtos:List[Produto] | None = None):
        self.produtos: List[Produto] = produtos if produtos else []

    @property
    def total(self):
        if len(self.produtos) > 0 :
            return sum(produto.preco for produto in self.produtos)
        return 0

    def __add__(self, other):
        if isinstance(other, Produto):
            self.produtos.append(other)
            return self

        if isinstance(other, Carrinho):
            self.produtos += other.produtos
            return self

        raise TypeError("Você tentou adicionar algo inválido ao carrinho.")


    def __str__(self):
        separador = "-" * 30 + "\n" 
        mensagem = separador
        if len(self.produtos) > 0:
            for produto in self.produtos:
                mensagem += f"{str(produto)}\n"
        mensagem += separador
        mensagem += f"Total: {formata_dinheiro(self.total)}"
        return mensagem



def formata_dinheiro(valor: float) -> str:
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return locale.currency(valor, grouping=True)