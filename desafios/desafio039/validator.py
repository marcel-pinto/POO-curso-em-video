from abc import ABC, abstractmethod
import re

class Validador(ABC):
    @abstractmethod
    def validar(self, valor):
        pass

# Requerimentos Usuario
# - de 5 a 20 caracteres
# - letras minusculas
# - numeros
# - Simbolo de sublinhado
class Usuario(Validador):
    def validar(self, valor):
        pattern = r"^[a-z0-9_]{5,20}$"
        return re.fullmatch(pattern, valor)

# Deve conter uma unica @
# Usuario pode conter letras, numeros e alguns simbolos
# os dominios contem pontos
# o top level domain encerra com ponto e pelo menos 2 letras
class Email(Validador):
    def validar(self, valor):
        pattern = r"^[^@\s]+@[^@\s.]+(?:\.[^@\s.]+)*\.[A-Za-z]{2,}\.[A-Za-z]{2,}$"
        return re.fullmatch(pattern, valor)


# - Pelo menos 8 caracteres
# - Pelo menos uma maiuscula
# - Pelo menos um simbolo
class Senha(Validador):
    def validar(self, valor):
        pattern = r"^(?=.*[A-Z])(?=.*[^A-Za-z0-9]).{8,}$"
        return re.fullmatch(pattern, valor)


def validar_dado(dado, valor):
    print(f"Valor: {valor} é válido? {'SIM' if dado.validar(valor) else 'NÃO'}")