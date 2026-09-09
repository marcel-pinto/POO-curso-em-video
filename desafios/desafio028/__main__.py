from termostato import Termostato
from rich import inspect

def main():
    t = Termostato()
    t.temperatura = 17.3
    inspect(t, private=True, methods=True)

if __name__ == "__main__":
    main()