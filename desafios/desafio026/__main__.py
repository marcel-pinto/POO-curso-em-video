from transportes import Moto, Caminhao, Drone
from rich import print
from rich.table import Table

def main():
    dist = 100

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title = "Tabela de Fretes")

    for column in ("Distancia", "Tipo", "Frete"):
        tabela.add_column(column)

    for entrega in viagem:
        tabela.add_row(f"{dist}Km", type(entrega).__name__, entrega.calc_frete())

    print(tabela)

if __name__ == "__main__":
    main()