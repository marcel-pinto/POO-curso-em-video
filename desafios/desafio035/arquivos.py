from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome:str, extensao:str, tamanho:int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = extensao

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ["pdf", "doc", "docx"]
        ext = ext.lower().strip()

        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError("O arquivo está em um formato não suportado")
        
    @property
    def nome_completo(self):
        return f"'{self.nome}' ({self.tamanho / 1_000_000:.2f} MB)"

    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):
    extensao = "pdf"
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, PDF.extensao, tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")

class DOC(Arquivo):
    extensao = "docx"
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, DOC.extensao, tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} noMicrosoft World")


def abrir_arquivo(arquivo):
    arquivo.abrir()