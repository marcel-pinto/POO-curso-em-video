from abc import ABC
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        hoje = datetime.today().year
        if 2000 <= ano <= hoje:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido.")

    @property
    def idade(self):
        hoje = datetime.today().year
        return hoje - self._nascimento 

    @idade.setter
    def idade(self, _):
        raise PermissionError("Você não pode alterar a idade. Mude o ano do nascimento")

class Aluno(Pessoa):
    cursos_oficiais = ["ADS", "ADM", "ENG", "CONT"]

    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, nome_curso):
        if nome_curso in Aluno.cursos_oficiais:
            self._curso = nome_curso
        else:
            raise ValueError(f"O curso {nome_curso} não está na lista de cursos oficiais.")

    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        if len(curso) < 3 or len(curso) > 5:
            raise ValueError("O nome do curso deve possuir de 3 a 5 caracteres.")

        if curso in Aluno.cursos_oficiais:
            raise ValueError(f"O curso {curso} já está na lista de cursos oficiais.")
        Aluno.cursos_oficiais.append(curso)

