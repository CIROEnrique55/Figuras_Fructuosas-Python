import math
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Necesita instalar Pillow: pip install pillow
import os

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

    def calcular():
        tipo_calculo = tipo_var.get().strip().lower()
        figura = figura_var.get().strip().lower()
        
        try:
            if figura == "cuadrado":
                lado = float(lado_entry.get())
                if tipo_calculo == "área":
                    resultado = area_cuadrado(lado)
                elif tipo_calculo == "perímetro":
                    resultado = perimetro_cuadrado(lado)
                else:
                    raise ValueError("Tipo de cálculo no válido.")
            elif figura in ["rectángulo", "rectangulo"]:
                base = float(base_entry.get())
                altura = float(altura_entry.get())
                if tipo_calculo == "área":
                    resultado = area_rectangulo(base, altura)
                elif tipo_calculo == "perímetro":
                    resultado = perimetro_rectangulo(base, altura)
                else:
                    raise ValueError("Tipo de cálculo no válido.")
            elif figura in ["triángulo equilátero", "triangulo equilatero"]:
                lado = float(lado_entry.get())
                if tipo_calculo == "área":
                    resultado = area_triangulo_equilatero(lado)
                elif tipo_calculo == "perímetro":
                    resultado = perimetro_triangulo_equilatero(lado)
                else:
                    raise ValueError("Tipo de cálculo no válido.")
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
                    raise ValueError("Figura no válida.")
                
                lado = float(lado_entry.get())
                if tipo_calculo == "área":
                    resultado = area_poligono_regular(lado, n_lados)
                elif tipo_calculo == "perímetro":
                    resultado = perimetro_poligono_regular(lado, n_lados)
                else:
                    raise ValueError("Tipo de cálculo no válido.")
            
            messagebox.showinfo("Resultado", f"El {tipo_calculo} del {figura} es: {resultado}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

 
    root = tk.Tk()
    root.title("Cálculo de Área y Perímetro")


    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "Titulo.jpg")
    print(f"Ruta de la imagen: {img_path}")  # Imprimir la ruta de la imagen para depuración

    try:
        img = Image.open(img_path)
        img = img.resize((300, 100), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        img_label = ttk.Label(root, image=img)
        img_label.pack(pady=10)
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se pudo encontrar la imagen en la ruta: {img_path}")
        return

    main_frame = ttk.Frame(root, padding="10 10 10 10")
    main_frame.pack(fill='x', expand=True)

    ttk.Label(main_frame, text="Tipo de Cálculo (área/perímetro):").grid(column=0, row=0, sticky=tk.W)
    tipo_var = tk.StringVar()
    tipo_entry = ttk.Entry(main_frame, width=20, textvariable=tipo_var)
    tipo_entry.grid(column=1, row=0)

    ttk.Label(main_frame, text="Figura (cuadrado/rectángulo/triángulo equilátero/pentágono/etc.):").grid(column=0, row=1, sticky=tk.W)
    figura_var = tk.StringVar()
    figura_entry = ttk.Entry(main_frame, width=20, textvariable=figura_var)
    figura_entry.grid(column=1, row=1)

    ttk.Label(main_frame, text="Lado:").grid(column=0, row=2, sticky=tk.W)
    lado_entry = ttk.Entry(main_frame, width=20)
    lado_entry.grid(column=1, row=2)

    ttk.Label(main_frame, text="Base (para rectángulo):").grid(column=0, row=3, sticky=tk.W)
    base_entry = ttk.Entry(main_frame, width=20)
    base_entry.grid(column=1, row=3)

    ttk.Label(main_frame, text="Altura (para rectángulo):").grid(column=0, row=4, sticky=tk.W)
    altura_entry = ttk.Entry(main_frame, width=20)
    altura_entry.grid(column=1, row=4)

    calcular_button = ttk.Button(main_frame, text="Calcular", command=calcular)
    calcular_button.grid(column=0, row=5, columnspan=2, pady=10)

 
    root.mainloop()

if __name__ == "__main__":
    calcular_area_perimetro()
