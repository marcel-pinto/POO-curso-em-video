from diario import Diario
from getpass import getpass
from rich import print

def main():
    d = Diario()
    d.escrever("Consegui fazer o exercicio")
    d.escrever("Não sou carioca")

    try:
        d.ler()
    except Exception as error:
        print(f"[red] Erro: {error}")

    # novasenha = getpass("Digite a nova senha: ")
    # d.senha = novasenha
if __name__ == "__main__":
    main()