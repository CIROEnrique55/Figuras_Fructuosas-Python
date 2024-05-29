import math

def calcular_area_perimetro():
    def area_cuadrado(lado):
        return round(lado ** 2, 2)

    def perimetro_cuadrado(lado):
        return lado * 4

    def area_rectangulo(base, altura):
        return round(base * altura, 2)

    def perimetro_rectangulo(base, altura):
        return 2 * (base + altura)

    def area_triangulo_equilatero(lado):
        return round((lado ** 2 * (3 ** 0.5)) / 4, 2)

    def perimetro_triangulo_equilatero(lado):
        return 3 * lado

    def area_poligono_regular(lado, n_lados):
        apotema = lado / (2 * math.tan(math.pi / n_lados))
        perimetro = n_lados * lado
        return round((perimetro * apotema) / 2, 2)

    def perimetro_poligono_regular(lado, n_lados):
        return n_lados * lado

    tipo_calculo = input("¿Qué desea obtener? (área/perímetro): ").strip().lower()
    figura = input("¿De qué figura regular? (cuadrado/rectángulo/triángulo equilátero/pentágono/hexágono/heptágono/octógono/eneágono/decágono): ").strip().lower()

    if figura == "cuadrado":
        lado = float(input("Ingrese el lado del cuadrado: "))
        if tipo_calculo == "area":
            resultado = area_cuadrado(lado)
        elif tipo_calculo == "perimetro":
            resultado = perimetro_cuadrado(lado)
        else:
            print("Tipo de cálculo no válido.")
            return
    elif figura == "rectángulo" or figura == "rectangulo":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        if tipo_calculo == "area":
            resultado = area_rectangulo(base, altura)
        elif tipo_calculo == "perimetro":
            resultado = perimetro_rectangulo(base, altura)
        else:
            print("Tipo de cálculo no válido.")
            return
    elif figura == "triángulo equilátero" or figura == "triangulo equilatero":
        lado = float(input("Ingrese el lado del triángulo equilátero: "))
        if tipo_calculo == "area":
            resultado = area_triangulo_equilatero(lado)
        elif tipo_calculo == "perimetro":
            resultado = perimetro_triangulo_equilatero(lado)
        else:
            print("Tipo de cálculo no válido.")
            return
    else:
        n_lados = {
            "pentágono": 5, "pentagono": 5,
            "hexágono": 6, "hexagono": 6,
            "heptágono": 7, "heptagono": 7,
            "octógono": 8, "octogono": 8,
            "eneágono": 9, "eneagono": 9,
            "decágono": 10, "decagono": 10
        }.get(figura, None)
        
        if n_lados is None:
            print("Figura no válida.")
            return
        
        lado = float(input(f"Ingrese el lado del {figura}: "))
        if tipo_calculo == "area":
            resultado = area_poligono_regular(lado, n_lados)
        elif tipo_calculo == "perimetro":
            resultado = perimetro_poligono_regular(lado, n_lados)
        else:
            print("Tipo de cálculo no válido.")
            return

    print(f"El {tipo_calculo} del {figura} es: {resultado}")

if __name__ == "__main__":
    calcular_area_perimetro()