from rich import print
from rich.panel import Panel

class Gamer:
    ficha_width = 40

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.games_favoritos = []

    def add_favoritos(self, game):
        self.games_favoritos.append(game)

    def ficha(self):
        mensagem = f"Nome real: [black on blue] {self.nome} [/]\n"
        mensagem += "Jogos Favoritos:\n"
        parsed_games = [f":video_game: [blue]{game}[/]" for game in sorted(self.games_favoritos, key=str.lower)]

        jogos_favoritos = "\n".join(parsed_games)
        mensagem += jogos_favoritos

        panel = Panel(mensagem, title=f"Jogador <{self.nick}>", width=Gamer.ficha_width)
        print(panel)


j1 = Gamer(nome = "Fabricio da Silva", nick = "detonator2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer(nome = "Olívia Souza", nick = "peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call of Duty")
j2.ficha()