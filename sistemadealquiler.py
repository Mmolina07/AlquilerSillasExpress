import tkinter as tk

def applicationSupportsSecureRestorableState() -> bool:
    return True

inventario_informales = 800
inventario_formales = 400
precio_silla_informal = 1500
precio_silla_formal = 3000

def mostrar_tarifas():
    tarifas_window = tk.Toplevel(main_window)
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

def calcular_precio(paquete, tipo_silla):
    if tipo_silla == "informal":
        precio_por_silla = precio_silla_informal
    else:
        precio_por_silla = precio_silla_formal
    
    if paquete < 15:
        precio = paquete * (precio_por_silla * 1.1)
    else:
        precio = paquete * precio_por_silla
    
    return precio

def seleccionar_paquete():
    tipo_silla = tipo_silla_var.get()
    
    if tipo_silla == "Informal":
        opciones = [1, 2, 3, 4, 5, 6]
    else:
        opciones = [7, 8, 9, 10, 11, 12]
    
    opcion = int(opcion_var.get())
    
    if opcion < 1 or opcion > 6:
        return
    
    cantidad = [15, 30, 45, 60, 75, 90][opcion - 1]
    
    if tipo_silla == "Informal":
        if inventario_informales < cantidad:
            return
    else:
        if inventario_formales < cantidad:
            return
    
    precio_total = calcular_precio(cantidad, tipo_silla)
    precio_label.config(text=f"El precio total es: ${precio_total}")
    
def devolver_sillas():
    tipo_silla = tipo_silla_devolver_var.get()
    cantidad = int(cantidad_devolver_var.get())
    
    if tipo_silla == "Informal":
        inventario_informales += cantidad
    else:
        inventario_formales += cantidad
    
    resultado_label.config(text=f"Se han devuelto {cantidad} sillas {tipo_silla}.\nAhora hay {inventario_informales} sillas informales y {inventario_formales} sillas formales en inventario.")

def main():
    global main_window, tipo_silla_var, opcion_var, precio_label, tipo_silla_devolver_var, cantidad_devolver_var, resultado_label

    main_window = tk.Tk()
    main_window.title("Sistema de alquiler de sillas")

    tipo_silla_var = tk.StringVar()
    opcion_var = tk.StringVar()
    tipo_silla_devolver_var = tk.StringVar()
    cantidad_devolver_var = tk.StringVar()

    frame = tk.Frame(main_window)
    frame.pack()

    tk.Label(frame, text="Sistema de alquiler de sillas", font=("Helvetica", 16)).grid(row=0, column=1, columnspan=2)

    tk.Button(frame, text="Mostrar tarifas", command=mostrar_tarifas).grid(row=1, column=1, columnspan=2)
    
    tk.Label(frame, text="Seleccione el tipo de silla:").grid(row=2, column=1, columnspan=2)
    tk.Radiobutton(frame, text="Informal", variable=tipo_silla_var, value="Informal").grid(row=3, column=1)
    tk.Radiobutton(frame, text="Formal", variable=tipo_silla_var, value="Formal").grid(row=3, column=2)

    tk.Label(frame, text="Seleccione el número de paquete que desea:").grid(row=4, column=1, columnspan=2)
    opciones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    tk.OptionMenu(frame, opcion_var, *opciones).grid(row=5, column=1, columnspan=2)
    
    tk.Button(frame, text="Calcular precio", command=seleccionar_paquete).grid(row=6, column=1, columnspan=2)
    precio_label = tk.Label(frame, text="", font=("Helvetica", 12))
    precio_label.grid(row=7, column=1, columnspan=2)

    tk.Label(frame, text="¿Desea devolver sillas?").grid(row=8, column=1, columnspan=2)
    tk.Radiobutton(frame, text="Informal", variable=tipo_silla_devolver_var, value="Informal").grid(row=9, column=1)
    tk.Radiobutton(frame, text="Formal", variable=tipo_silla_devolver_var, value="Formal").grid(row=9, column=2)
    tk.Label(frame, text="Cantidad a devolver:").grid(row=10, column=1)
    tk.Entry(frame, textvariable=cantidad_devolver_var).grid(row=10, column=2)
    
    tk.Button(frame, text="Devolver sillas", command=devolver_sillas).grid(row=11, column=1, columnspan=2)
    resultado_label = tk.Label(frame, text="", font=("Helvetica", 12))
    resultado_label.grid(row=12, column=1, columnspan=2)

    tk.Button(frame, text="Salir", command=main_window.quit).grid(row=13, column=1, columnspan=2)

    main_window.mainloop()

if __name__ == "__main__":
    main()
