from hashlib import sha256
from rich import print
class Credencial:
    def __init__(self):
        self.__hash_senha = ""

    @property
    def senha(self):
        return self.__hash_senha

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash_senha = sha256(chave.encode("utf-8")).hexdigest()
        else:
            raise ValueError("A senha precisa ter pelo menos 1 caractere")
    def validar(self, senha):
        hash = sha256(senha.encode("utf-8")).hexdigest()

        if hash == self.__hash_senha:
            print("[green]Senha correta![/]")
            return True
        else:
            print("[red]Senha incorreta![/]")
            return False