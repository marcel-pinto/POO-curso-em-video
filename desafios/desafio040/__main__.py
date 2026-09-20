from exportador_dados import *

def main():
    u = [
        Usuario('Pedro', "pedro@gmail.com"),
        Usuario('Maria', "marizinha@hotmail.com"),
    ]

    a = [
        Aluno("Cláudia", "ADS", "2 per"),
        Aluno("Ana", "ADM", "4 per"),
        Aluno("Mario", "SEG", "1 per")
    ]
    # exportar_dados(XML(), Usuario('Pedro', "pedro@gmail.com"))
    exportar_dados(JSON(), u)
    exportar_dados(JSON(), a)
if __name__ == '__main__':
    main()