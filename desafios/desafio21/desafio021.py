from rich import print

class Caneta:
    cores = {
        "azul": "blue",
        "vermelha": "red",
        "verde": "green",
        "amarela": "yellow"
    }

    def __init__(self, cor):
        self.cor = cor.lower()
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, texto):
        cor_caneta = Caneta.cores[self.cor]
        if self.tampada:
            print(f":no_entry_sign: A [{cor_caneta}]caneta[/] está tampada!")
        else:
            print(f"[{cor_caneta}]{texto}[/]", end="")

    def quebrar_linha(self, linhas):
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