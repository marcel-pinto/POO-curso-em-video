from termostato import Termostato
from rich import inspect

def main():
    t = Termostato()
    try:
        t.temperatura = 25.2
    except Exception as erro:
        print(f"Houve um problema: {erro}")

    print(f"A temperatura atual é {t.ftemperatura}.")
if __name__ == "__main__":
    main()