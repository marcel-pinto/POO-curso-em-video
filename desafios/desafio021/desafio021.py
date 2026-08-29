from rich import print

class Caneta:
    def __init__(self, cor):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"

        self.cor = escolha
        self.tampada = True

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, texto):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!")
        else:
            print(f"{self.cor}{texto}[/]", end="")

    def quebrar_linha(self, linhas = 1):
        print("\n" * linhas, end="")


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto! ")
c3.escrever("Vamos, exercitar!")