from abc import ABC, abstractmethod
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

    @abstractmethod
    def pagar(self):
        pass


class Boleto(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            # ... Codigo pagamento....
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Boleto")
        except Exception as e:
            print(f"Falha no pagamento de {self.fvalor} via Boleto.")


class PIX(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
                # ... Codigo pagamento....
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Pix")
        except Exception as e:
            print(f"Falha no pagamento de {self.fvalor} via Pix.")


class Credito(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            # ... Codigo pagamento....
            print(f"Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito")
        except Exception as e:
            print(f"Falha no pagamento de {self.fvalor} via Cartão de Crédito.")

def finalizar_compra(pagamento: Pagamento, valor: float):
    pagamento.pagar(valor)