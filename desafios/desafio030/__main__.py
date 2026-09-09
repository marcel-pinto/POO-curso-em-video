from credencial import Credencial
from rich import print
from getpass import getpass

def main():
    c = Credencial()
    c.senha = getpass("Digite sua senha: ")
    print("Senha salva com sucesso!")

    c.validar(getpass("Digite sua senha para validar: "))

if __name__ == "__main__":
    main()