from rich import print
from getpass import getpass

class Diario:
    def __init__(self, senha = "CeV!@"):
        self.__segredos = []
        self.__senha = senha


    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha = None):
        if not senha:
            senha = getpass("Por favor digite sua senha: ")

        if senha != self.__senha:
            print("Senha inválida!")
        else:
            print("[green]DIARIO LIBERADO[/]")
            for segredo in self.__segredos:
                print(f"- {segredo}")