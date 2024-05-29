def calcular_area_perimetro():
    def area_cuadrado(lado):
        return lado ** 2

    def perimetro_cuadrado(lado):
        return 4 * lado

    def area_rectangulo(base, altura):
        return base * altura

    def perimetro_rectangulo(base, altura):
        return 2 * (base + altura)

    def area_triangulo_equilatero(lado):
        return (lado ** 2 * (3 ** 0.5)) / 4

    def perimetro_triangulo_equilatero(lado):
        return 3 * lado

    tipo_calculo = input("¿Qué desea obtener? (área/perímetro): ").strip().lower()
    figura = input("¿De qué figura regular? (cuadrado/rectángulo/triángulo equilátero): ").strip().lower()

    if figura == "cuadrado":
        lado = float(input("Ingrese el lado del cuadrado: "))
        if tipo_calculo == "área":
            resultado = area_cuadrado(lado)
        elif tipo_calculo == "perímetro":
            resultado = perimetro_cuadrado(lado)
        else:
            print("Tipo de cálculo no válido.")
            return
    elif figura == "rectángulo" or figura == "rectangulo":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        if tipo_calculo == "área":
            resultado = area_rectangulo(base, altura)
        elif tipo_calculo == "perímetro":
            resultado = perimetro_rectangulo(base, altura)
        else:
            print("Tipo de cálculo no válido.")
            return
    elif figura == "triángulo equilátero" or figura == "triangulo equilatero":
        lado = float(input("Ingrese el lado del triángulo equilátero: "))
        if tipo_calculo == "área":
            resultado = area_triangulo_equilatero(lado)
        elif tipo_calculo == "perímetro":
            resultado = perimetro_triangulo_equilatero(lado)
        else:
            print("Tipo de cálculo no válido.")
            return
    else:
        print("Figura no válida.")
        return

    print(f"El {tipo_calculo} del {figura} es: {resultado}")

if __name__ == "__main__":
    calcular_area_perimetro()