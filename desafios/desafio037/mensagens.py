from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, mensagem : str, icone : str= ":speech_balloon:", tipo : str = "AVISO"):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    def mostrar(self, width=60):
        title = f"{self._icone} {self._tipo.upper()} {self._icone}"
        print(
            Panel(self._mensagem, title=title, width=width, style="#ffffff on #000000")
            )

class Erro(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem, icone = ":prohibited:", tipo = "ERRO")

    def mostrar(self, width=60):
        title = f"{self._icone} {self._tipo} {self._icone}"
        print(
            Panel(f"{self._mensagem}", title=title, width=width, style="#ffff00 on #880000")
            )

        
class Alerta(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem, icone = ":warning:", tipo= "ALERTA")

    def mostrar(self, width=60):
        title = f"{self._icone} {self._tipo} {self._icone}"
        print(
            Panel(f"{self._mensagem}", title=title, width=width, style="#000000 on #fffc1b")
            )