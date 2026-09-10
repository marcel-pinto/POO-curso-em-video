from retangulo import Retangulo
from rich import inspect
def main():
    r = Retangulo()
    r.base = 4
    r.altura = 5

    r.medidas = (4,5)
    print(r.medidas)
    inspect(r, private=True)


if __name__ == "__main__":
    main()