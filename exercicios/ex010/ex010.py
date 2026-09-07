class Avaliacao:

    def __init__(self, nome, disciplina, nota =0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protected(#)

    @property
    def nota(self): # Getter
        return self._nota

    @nota.setter
    def nota(self, valor): # Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota invalida!")

    @nota.deleter
    def nota(self):
        pass

    
    # Metodos acessores
    def get_nota(self):
        return self._nota

    def set_nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota invalida!")