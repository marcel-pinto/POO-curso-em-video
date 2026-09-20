from validator import Usuario, Email, Senha, validar_dado

def main():
    validar_dado(Usuario(), "gs1234")
    validar_dado(Email(), "aaa@gmail.com.bt")
    validar_dado(Senha(), "Testando1234#")

if __name__ == "__main__":
    main()