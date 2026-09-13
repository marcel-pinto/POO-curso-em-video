from arquivos import *

def main():
    a1 = DOC(nome="Prova", tamanho=250_000)
    a2 = PDF(nome="Contrato", tamanho=1_350_000)

    abrir_arquivo(a1)
    abrir_arquivo(a2)

    print(a2.nome_completo)

if __name__ == "__main__":
    main()