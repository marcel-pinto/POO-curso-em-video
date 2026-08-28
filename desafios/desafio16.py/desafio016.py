from rich import print
from rich import inspect

class Funcionario:
    # Atributos de classe
    empresa = "Curso em Video"
    def __init__(self, nome, setor, cargo):
        # Atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}."


#Funcionario.empresa = "Hostnet"

c1 = Funcionario(nome="Maria", setor="Admnistração", cargo = "Diretora")
print(c1.apresentacao())

c2 = Funcionario(nome="Pedro", setor="TI", cargo="Programador")
print(c2.apresentacao())

