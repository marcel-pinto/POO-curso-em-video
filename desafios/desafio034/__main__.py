from funcionarios import Designer, Desenvolvedor, Gerente

def main():
    f = Desenvolvedor("Pedro", 1800)
    f.salario = 1000
    print(f)

if __name__ == "__main__":
    main()