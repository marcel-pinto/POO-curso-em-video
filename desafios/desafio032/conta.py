from getpass import getpass
from hashlib import sha256

class ContaBancaria:
    def __init__(self, id:int, nome:str = None, saldo:float = 0., chave:str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo

        if not chave:
            chave = self.pede_senha()

        self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        print(f"Conta {id} foi criada com sucesso. Saldo atual R${saldo:,.2f}.")

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"
    
    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novo_nome):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            self._titular = novo_nome

    def validar_senha(self, chave):
        hash = sha256(chave.encode("utf-8")).hexdigest()
        if hash == self.__hash:
            return True
        else:
            print("Senha Inválida!")
            return False

    def pede_senha(self):

        while True:
            senha = getpass("Senha: ")
            if len(senha) >= 6:
                break
        return senha

    def sacar(self, valor, chave = None):
        if valor <= 0:
            raise ValueError("O valor sacado precisa ser maior que zero.")

        if not chave:
            chave = self.pede_senha()
        
        if self.validar_senha(chave):
            if self.__saldo > valor:
                self.__saldo -= valor
                print(f"Saque realizado na conta {self._id} com sucesso. Saldo atual R${self.__saldo:,.2f}.")
            else:
                raise ValueError(f"Saque na conda {self._id} recusado! Saldo insuficiente.")
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito realizado na conta {self._id} com sucesso. Saldo atual R${self.__saldo:,.2f}.")
        else:
            raise ValueError("O valor depositado precisa ser maior que zero.")