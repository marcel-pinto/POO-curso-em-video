from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, mensagem : str, icone : str= ":speech_balloon:", tipo : str = "AVISO"):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    def mostrar(self, width=60):
        title = f"{self._icone} {self._tipo} {self._icone}"
        print(
            Panel(self._mensagem, title=title, width=width, style="white on black")
            )

class Erro(Mensagem):
    def __init__(self, mensagem, icone=":prohibited:", tipo="ERRO"):
        super().__init__(mensagem, icone, tipo)

    def mostrar(self, width=60):
        title = f"[yellow]{self._icone} {self._tipo} {self._icone}[/]"
        print(
            Panel(f"[yellow on red]{self._mensagem}[/]", title=title, width=width, style="yellow on red")
            )

        
class Alerta(Mensagem):
    def __init__(self, mensagem, icone=":warning:", tipo="ALERTA"):
        super().__init__(mensagem, icone, tipo)

    def mostrar(self, width=60):
        title = f"{self._icone} {self._tipo} {self._icone}"
        print(
            Panel(f"{self._mensagem}", title=title, width=width, style="black on yellow")
            )