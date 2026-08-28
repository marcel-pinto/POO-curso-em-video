from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo, empresa="Curso em Video"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentacao(self):
        return f":handshake: Olá sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}."



c1 = Funcionario(nome="Maria", setor="Admnistração", cargo = "Diretora")
print(c1.apresentacao())

c2 = Funcionario(nome="Pedro", setor="TI", cargo="Programador")
print(c2.apresentacao())