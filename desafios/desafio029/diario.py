from rich import print
from getpass import getpass

class Diario:
    def __init__(self, senha = "CeV!@"):
        self.__segredos = []
        self.__senha = senha.strip()


    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha = None):
        if not senha:
            senha = getpass("Por favor digite sua senha: ")

        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")
        else:
            print("[green]DIARIO LIBERADO[/]")
            for segredo in self.__segredos:
                print(f"- {segredo}")

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha.")

    @senha.setter
    def senha(self, novasenha):
        senha = getpass("Digite a senha antiga: ")
        if senha == self.__senha:
            self.__senha = senha
            print("Senha alterada com sucesso.")
        else:
            print("A senha antiga não está correta.")