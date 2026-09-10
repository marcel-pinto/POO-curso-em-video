from retangulo import Retangulo
from rich import inspect
def main():

    r = Retangulo(7, 4)
    try:
        r.base = 12
        r.altura=7
        r.medidas=(8,12)
    except Exception as error:
        print(f"Ocorreu um erro do tipo {type(error).__name__}: {error}")

    print(r.medidas)

if __name__ == "__main__":
    main()