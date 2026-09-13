from funcionarios import Designer, Desenvolvedor, Gerente

def main():
    # f = Desenvolvedor("Pedro", 1800)
    # print(f)
    # try:
    #     f.salario = 100
    # except Exception as e:
    #     print(f"Não foi possivel alterar o salario: ERRO {e}")

    funcionarios = [
        Desenvolvedor("Pedro", salario=18_000),
        Designer("José", salario=25_000),
        Gerente("Mariana", salario=45_000)
    ]

    for f in funcionarios:
        print(f)

if __name__ == "__main__":
    main()