from hashlib import sha256
from rich import print
class Credencial:
    def __init__(self):
        self.__hash_senha = ""

    @property
    def senha(self):
        return self.__hash_senha

    @senha.setter
    def senha(self, valor):
        self.__hash_senha = sha256(valor.encode()).hexdigest()

    def validar(self, senha):
        hash = sha256(senha.encode()).hexdigest()

        if hash == self.__hash_senha:
            print("[green]Senha correta![/]")
        else:
            print("[red]Senha incorreta![/]")