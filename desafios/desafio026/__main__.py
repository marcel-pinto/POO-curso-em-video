from funcionarios import Horista, Mensalista

def main():
    f1 = Horista(nome = "Paulo", valor_hora = 12, horas_trab= 200)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = Mensalista(nome = "Amanda", salario_bruto=9500)
    f2.calcular_salario()
    f2.analisar_salario()
    
if __name__ == "__main__":
    main()