from abc import ABC
from datetime import datetime

class Pessoa:
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        hoje = datetime.today().year
        if ano > hoje or ano < 2000:
            raise ValueError(f"Ano {ano} é inválido.")
        else:
            self._nascimento = ano

    @property
    def idade(self):
        hoje = datetime.today().year
        return hoje - self._nascimento 

    @idade.setter
    def idade(self, _):
        raise PermissionError("Você não pode alterar a idade. Mude o ano do nascimento")

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self._curso = None
        self.cursos_oficiais = ["ADS", "ADM", "ENG", "CONT"]
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, nome_curso):
        if nome_curso in self.cursos_oficiais:
            self._curso = nome_curso
        else:
            raise ValueError(f"O curso {nome_curso} não está na lista de cursos oficiais.")

    def add_curso(self, curso:str):
        if len(curso) < 3 or len(curso) > 5:
            raise ValueError("O nome do curso deve possuir de 3 a 5 caracteres.")
        else:
            self.cursos_oficiais.append(curso.upper())

