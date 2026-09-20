import json
from functools import singledispatchmethod
import xml.etree.ElementTree as ET

class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class JSON:
    @singledispatchmethod
    def exportar(self, dado):
        return json.dumps(dado.__dict__, indent=4)

    @exportar.register
    def _(self, dado: list):
        return json.dumps([d.__dict__ for d in dado], indent=4)

class XML:
    @singledispatchmethod
    def exportar(self, dado):
        root = ET.Element('dado')
        for key, value in dado.__dict__.items():
            ET.SubElement(root, key).text = str(value)

        ET.indent(root, space=" " * 4)
        return ET.tostring(root,  encoding="unicode")

    @exportar.register
    def _(self, dados: list):
        root = ET.Element('dados')
        for dado in dados:
            user = ET.SubElement(root, dado.__class__.__name__.lower())
            for key, value in dado.__dict__.items():
                ET.SubElement(user, key).text = str(value)

        ET.indent(root, space=" " * 4)
        return ET.tostring(root,  encoding="unicode")


def exportar_dados(tipo, dados):
    print(tipo.exportar(dados))