import tkinter as tk


inventario_informales = 800
inventario_formales = 400
precio_silla_informal = 1500
precio_silla_formal = 3000

def mostrar_tarifas():
    print("Tarifas:")
    print("1. Paquete de 15 sillas informales: $22,500")
    print("2. Paquete de 30 sillas informales: $45,000")
    print("3. Paquete de 45 sillas informales: $67,500")
    print("4. Paquete de 60 sillas informales: $90,000")
    print("5. Paquete de 75 sillas informales: $112,500")
    print("6. Paquete de 90 sillas informales: $135,000")
    print("7. Paquete de 15 sillas formales: $45,000")
    print("8. Paquete de 30 sillas formales: $90,000")
    print("9. Paquete de 45 sillas formales: $135,000")
    print("10. Paquete de 60 sillas formales: $180,000")
    print("11. Paquete de 75 sillas formales: $225,000")
    print("12. Paquete de 90 sillas formales: $270,000")

def mostrar_tarifas_en_interfaz():
    texto_a_mostrar = mostrar_tarifas()
    resultado_text.delete("1.0", "end")
    resultado_text.insert("1.0", texto_a_mostrar)

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
    global inventario_informales, inventario_formales
    tipo_silla = str(input("¿Desea sillas informales o formales? (informal/formal): "))
    
    if tipo_silla == "informal":
        print("1. Paquete de 15 sillas informales: $22,500")
        print("2. Paquete de 30 sillas informales: $45,000")
        print("3. Paquete de 45 sillas informales: $67,500")
        print("4. Paquete de 60 sillas informales: $90,000")
        print("5. Paquete de 75 sillas informales: $112,500")
        print("6. Paquete de 90 sillas informales: $135,000")
    elif tipo_silla == "formal":
        print("7. Paquete de 15 sillas formales: $45,000")
        print("8. Paquete de 30 sillas formales: $90,000")
        print("9. Paquete de 45 sillas formales: $135,000")
        print("10. Paquete de 60 sillas formales: $180,000")
        print("11. Paquete de 75 sillas formales: $225,000")
        print("12. Paquete de 90 sillas formales: $270,000")
    
    else:
        print("Opcion no valida!")
        main()

    try:
        opcion = int(input("Seleccione el número de paquete que desea: "))

    except (ValueError, UnboundLocalError):
        print("Digite una opcion valida")

    if opcion < 1 or opcion > 12:
        print("Opción no válida")
        return
    
    cantidad = [15, 30, 45, 60, 75, 90, 15, 30, 45, 60, 75, 90][opcion - 1]
    
    if tipo_silla == "informal":
        if inventario_informales < cantidad:
            print("No hay suficientes sillas informales en el inventario.")
            return
    else:
        if inventario_formales < cantidad:
            print("No hay suficientes sillas formales en el inventario.")
            return
    
    precio_total = calcular_precio(cantidad, tipo_silla)
    print(f"El precio total es: ${precio_total}")
    
    confirmacion = input("¿Desea comprar este paquete? (si/no): ")
    if confirmacion.lower() == "si":
        if tipo_silla == "informal":
            inventario_informales -= cantidad
        else:
            inventario_formales -= cantidad
        print(f"Compra exitosa. Quedan {inventario_informales} sillas informales y {inventario_formales} sillas formales en inventario.")
    else:
        print("Compra cancelada.")


def devolver_sillas():
    global inventario_informales, inventario_formales
    tipo_silla = input("¿Desea devolver sillas informales o formales? (informal/formal): ")
    cantidad = int(input("Ingrese la cantidad de sillas que desea devolver: "))
    
    if tipo_silla == "informal":
        inventario_informales += cantidad
    else:
        inventario_formales += cantidad
    
    print(f"Se han devuelto {cantidad} sillas {tipo_silla}.")
    print(f"Ahora hay {inventario_informales} sillas informales y {inventario_formales} sillas formales en inventario.")

def main():
    while True:
        print("\nSistema de alquiler de sillas")
        print("1. Mostrar tarifas")
        print("2. Seleccionar paquete")
        print("3. Devolver sillas")
        print("4. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            mostrar_tarifas()
        elif opcion == 2:
            seleccionar_paquete()
        elif opcion == 3:
            devolver_sillas()
        elif opcion == 4:
            print("Gracias por usar el sistema de alquiler de sillas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida")

def seleccionar_paquete_event():
    tipo_silla = tipo_silla_var.get()
    opcion = opcion_var.get()
    if tipo_silla and opcion:
        seleccionar_paquete()
        update_inventory_label()

def devolver_sillas_event():
    tipo_silla = tipo_silla_var.get()
    cantidad = cantidad_devolver_entry.get()
    if tipo_silla and cantidad:
        devolver_sillas()
        update_inventory_label()

def update_inventory_label():
    inventario_label.config(text=f"Inventario: Informales: {inventario_informales}, Formales: {inventario_formales}")

# Crear la ventana
window = tk.Tk()
window.title("Sistema de Alquiler de Sillas")

# Variables
tipo_silla_var = tk.StringVar()
opcion_var = tk.IntVar()

# Crear elementos de la interfaz
mostrar_button = tk.Button(window, text="Mostrar Paquetes", command=mostrar_tarifas_en_interfaz)
mostrar_button.pack()

resultado_text = tk.Text(window, wrap=tk.WORD, height=10, width=40)
resultado_text.pack()

tipo_silla_label = tk.Label(window, text="¿Desea sillas informales o formales?")
tipo_silla_label.pack()

informal_radio = tk.Radiobutton(window, text="Informales", variable=tipo_silla_var, value="informal")
informal_radio.pack()
formal_radio = tk.Radiobutton(window, text="Formales", variable=tipo_silla_var, value="formal")
formal_radio.pack()

opcion_label = tk.Label(window, text="Seleccione el número de paquete que desea:")
opcion_label.pack()

for i in range(1, 13):
    opcion_radio = tk.Radiobutton(window, text=f"Opción {i}", variable=opcion_var, value=i)
    opcion_radio.pack()

seleccionar_button = tk.Button(window, text="Seleccionar Paquete", command=seleccionar_paquete_event)
seleccionar_button.pack()

cantidad_devolver_label = tk.Label(window, text="Cantidad de sillas a devolver:")
cantidad_devolver_label.pack()

cantidad_devolver_entry = tk.Entry(window)
cantidad_devolver_entry.pack()

devolver_button = tk.Button(window, text="Devolver Sillas", command=devolver_sillas_event)
devolver_button.pack()

mostrar_button = tk.Button(window, text="Mostrar Paquetes", command=mostrar_tarifas)
mostrar_button.pack()

inventario_label = tk.Label(window, text="Inventario: Informales: 800, Formales: 400")
inventario_label.pack()

mostrar_tarifas()

# Ejecutar la interfaz
window.mainloop()