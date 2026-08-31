from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):
    golpes = []

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, alvo, forca):
        print(f"[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red]{alvo.nome}[/]([cyan]{alvo.vida}[/]) com um [blue]{random.choice(self.__class__.golpes)}[/] de forca [cyan]{forca}[/]")
        dano = random.randint(0, forca)
        alvo.receber_dano(dano)
        print(f"[blue]{alvo.nome}[/] recebou [red]dano de {dano}[/]")

    def receber_dano(self, dano):
        self.vida -= dano

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    golpes = ["Soco", "Pulo Giratório"]

    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        cura = random.randint(0, 100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida.")

class Mago(Personagem):
    golpes = ["Bola de Fogo"]

    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        cura = random.randint(0, 100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida.")

