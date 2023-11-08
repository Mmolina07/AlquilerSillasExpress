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