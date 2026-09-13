from abc import ABC

class Arquivo(ABC):
    def __init__(self, nome:str, extensao:str, tamanho:int):
        self.nome = nome
        self._extensao = extensao
        self.tamanho = tamanho

    @property
    def nome_completo(self):
        return f"'{self.nome}' ({self.tamanho / 1_000_000:.2f} MB)"

    def abrir(self):
        pass


class PDF(Arquivo):
    extensao = "pdf"
    def __init__(self, nome, tamanho):
        super().__init__(nome, PDF.extensao, tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")

class DOC(Arquivo):
    extensao = "docx"
    def __init__(self, nome, tamanho):
        super().__init__(nome, DOC.extensao, tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} noMicrosoft World")


def abrir_arquivo(arquivo):
    arquivo.abrir()