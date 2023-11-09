import tkinter as tk

class SillaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de alquiler de sillas")
        
        self.inventario_informales = 800
        self.inventario_formales = 400
        self.precio_silla_informal = 1500
        self.precio_silla_formal = 3000

        self.create_widgets()

    def mostrar_tarifas(self):
        tarifas_window = tk.Toplevel(self.root)
        tarifas_window.title("Tarifas")
        
        tarifas_text = """
        Tarifas:
        1. Paquete de 15 sillas informales: $22,500
        2. Paquete de 30 sillas informales: $45,000
        3. Paquete de 45 sillas informales: $67,500
        4. Paquete de 60 sillas informales: $90,000
        5. Paquete de 75 sillas informales: $112,500
        6. Paquete de 90 sillas informales: $135,000
        7. Paquete de 15 sillas formales: $45,000
        8. Paquete de 30 sillas formales: $90,000
        9. Paquete de 45 sillas formales: $135,000
        10. Paquete de 60 sillas formales: $180,000
        11. Paquete de 75 sillas formales: $225,000
        12. Paquete de 90 sillas formales: $270,000
        """
        
        tarifas_label = tk.Label(tarifas_window, text=tarifas_text)
        tarifas_label.pack()

    def calcular_precio(self, paquete, tipo_silla):
        if tipo_silla == "informal":
            precio_por_silla = self.precio_silla_informal
        else:
            precio_por_silla = self.precio_silla_formal
        
        if paquete < 15:
            precio = paquete * (precio_por_silla * 1.1)
        else:
            precio = paquete * precio_por_silla
        
        return precio

    def seleccionar_paquete(self):
        tipo_silla = self.tipo_silla_var.get()
        
        if tipo_silla == "Informal":
            opciones = [1, 2, 3, 4, 5, 6]
        else:
            opciones = [7, 8, 9, 10, 11, 12]
        
        opcion = int(self.opcion_var.get())
        
        if opcion < 1 or opcion > 6:
            return
        
        cantidad = [15, 30, 45, 60, 75, 90][opcion - 1]
        
        if tipo_silla == "Informal":
            if self.inventario_informales < cantidad:
                return
        else:
            if self.inventario_formales < cantidad:
                return
        
        precio_total = self.calcular_precio(cantidad, tipo_silla)
        self.precio_label.config(text=f"El precio total es: ${precio_total}")

    def devolver_sillas(self):
        tipo_silla = self.tipo_silla_devolver_var.get()
        cantidad = int(self.cantidad_devolver_var.get())
        
        if tipo_silla == "Informal":
            self.inventario_informales += cantidad
        else:
            self.inventario_formales += cantidad
        
        self.resultado_label.config(text=f"Se han devuelto {cantidad} sillas {tipo_silla}.\nAhora hay {self.inventario_informales} sillas informales y {self.inventario_formales} sillas formales en inventario.")

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text="Sistema de alquiler de sillas", font=("Helvetica", 16)).grid(row=0, column=1, columnspan=2)

        tk.Button(frame, text="Mostrar tarifas", command=self.mostrar_tarifas).grid(row=1, column=1, columnspan=2)
        
        tk.Label(frame, text="Seleccione el tipo de silla:").grid(row=2, column=1, columnspan=2)
        self.tipo_silla_var = tk.StringVar()
        tk.Radiobutton(frame, text="Informal", variable=self.tipo_silla_var, value="Informal").grid(row=3, column=1)
        tk.Radiobutton(frame, text="Formal", variable=self.tipo_silla_var, value="Formal").grid(row=3, column=2)

        tk.Label(frame, text="Seleccione el número de paquete que desea:").grid(row=4, column=1, columnspan=2)
        self.opcion_var = tk.StringVar()
        opciones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        tk.OptionMenu(frame, self.opcion_var, *opciones).grid(row=5, column=1, columnspan=2)
        
        tk.Button(frame, text="Calcular precio", command=self.seleccionar_paquete).grid(row=6, column=1, columnspan=2)
        self.precio_label = tk.Label(frame, text="", font=("Helvetica", 12))
        self.precio_label.grid(row=7, column=1, columnspan=2)

        tk.Label(frame, text="¿Desea devolver sillas?").grid(row=8, column=1, columnspan=2)
        self.tipo_silla_devolver_var = tk.StringVar()
        tk.Radiobutton(frame, text="Informal", variable=self.tipo_silla_devolver_var, value="Informal").grid(row=9, column=1)
        tk.Radiobutton(frame, text="Formal", variable=self.tipo_silla_devolver_var, value="Formal").grid(row=9, column=2)
        tk.Label(frame, text="Cantidad a devolver:").grid(row=10, column=1)
        self.cantidad_devolver_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.cantidad_devolver_var).grid(row=10, column=2)
        
        tk.Button(frame, text="Devolver sillas", command=self.devolver_sillas).grid(row=11, column=1, columnspan=2)
        self.resultado_label = tk.Label(frame, text="", font=("Helvetica", 12))
        self.resultado_label.grid(row=12, column=1, columnspan=2)

        tk.Button(frame, text="Salir", command=self.root.quit).grid(row=13, column=1, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = SillaApp(root)
    root.mainloop()

