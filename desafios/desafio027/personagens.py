from abc import ABC, abstractmethod
import random
from rich import print
from rich.panel import Panel

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        if self.vida > 0 and alvo.vida > 0:
            print(f"[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red]{alvo.nome}[/]([cyan]{alvo.vida}[/]) com um [blue]{random.choice(self.golpes)}[/] de forca [cyan]{forca}[/]")
            alvo.receber_dano(forca)
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer.")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0.

        print(f"[blue]{self.nome}[/] recebou [red]dano de {dano}[/]")

    def status(self, width=40):
        message = f"Vida: {self.vida}\n"
        message += "Golpes:\n"
        message += "\n".join([f"   {golpe}" for golpe in self.golpes])
        panel = Panel(message, title=self.nome, width=width)
        print(panel)
    
    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Pulo Giratório", "Golpe de Machado"]

    def curar(self):
        cura = random.randint(0, 100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida.")

class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio de luz", "Magia Estática"]
        
    def curar(self):
        cura = random.randint(0, 100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida.")

