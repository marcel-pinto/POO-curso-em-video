from abc import ABC
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("O valor do pagamento deve ser maior que zero.")

        self._valor = novo_valor

    @property
    def fvalor(self):
        return locale.currency(self._valor, grouping=True)

    def pagar(self):
        pass


class Boleto(Pagamento):
    def __init__(self):
        super().__init__()

    def pagar(self):
        if self.valor:
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Boleto")


class PIX(Pagamento):
    def __init__(self):
        super().__init__()

    def pagar(self):
        if self.valor:
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Pix")



class Credito(Pagamento):
    def __init__(self):
        super().__init__()

    def pagar(self):
        if self.valor:
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito")

def finalizar_compra(pagamento, valor):
    pagamento.valor = valor
    pagamento.pagar()