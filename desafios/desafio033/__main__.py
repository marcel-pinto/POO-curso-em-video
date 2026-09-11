from classe33 import Aluno
from rich import inspect

def main():
    a1 = Aluno(nome="Maria", nascimento= 2000, curso="ADS")

    a1.nascimento = 2000
    a1.add_curso("MODA")
    a1.curso = "MODA"

    inspect(a1, private=True)
if __name__ == "__main__":
    main()