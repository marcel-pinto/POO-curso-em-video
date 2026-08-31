from poligonos import Quadrado, Circulo

def main():
    p1 = Quadrado(12)
    c1 = Circulo(20)

    print("Quadrado:")
    print(f"Perímetro = {p1.perimetro():.1f}")
    print(f"Area = {p1.area():.1f}\n")

    print("Circulo")
    print(f"Perímetro = {c1.perimetro():.1f}")
    print(f"Area = {c1.area():.1f}")


if __name__ == "__main__":
    main()