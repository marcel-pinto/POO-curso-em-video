from ex008 import ContaBancaria

def main():
    c1 = ContaBancaria(111, "Maria", 5000)
    c1.depositar(1000)
    print(c1)

if __name__ == "__main__":
   main()