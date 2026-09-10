from conta import ContaBancaria

def main():
    cc = ContaBancaria(id = 123, nome = "Marcelo", saldo = 1000, chave="123456")
    cc.nome = "João"
    cc.depositar(100)
    cc.sacar(100)
if __name__ == "__main__":
    main()