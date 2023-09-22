from datetime import datetime
from silla import Silla
from usuario import Usuario
from tarifas import Tarifas
from sistemaalquiler import SistemaAlquiler

class SistemaAlquiler:
    def __init__(self):
        self.sillas = []
        self.usuarios = []
        self.transacciones = []
        self.tarifas = Tarifas()
        self.registrar_sillas_disponibles()

    def registrar_silla(self, numero_serie, modelo, tarifa_por_hora):
        silla = Silla(numero_serie, modelo)
        self.tarifas.agregar_tarifa(numero_serie, tarifa_por_hora)
        self.sillas.append(silla)

    def registrar_sillas_disponibles(self):
        seriales_disponibles = ["S001", "S002", "S003", "S004", "S005", "S006", "S007", "S008", "S009", "S010"]
        for serial in seriales_disponibles:
            self.registrar_silla(serial, "Modelo Ejemplo", 2.0)

    def registrar_usuario(self, nombre, correo, identificacion):
        usuario = Usuario(nombre, correo, identificacion)
        self.usuarios.append(usuario)

    def alquilar_sillas(self, usuario, numero_serie, cantidad):
        sillas_alquiladas = []
        for _ in range(cantidad):
            if self.cantidad_sillas_disponibles > 0:
                for silla in self.sillas:
                    if silla.numero_serie == numero_serie and silla.disponible:
                        silla.alquilar()
                        sillas_alquiladas.append(silla)
                        self.transacciones.append((usuario, silla, datetime.now()))
                        self.cantidad_sillas_disponibles -= 1
                        break 
        return sillas_alquiladas

    def devolver_silla(self, usuario, numero_serie):
        for usuario, silla, inicio_alquiler in self.transacciones:
            if silla.numero_serie == numero_serie and usuario == usuario and not silla.disponible:
                inicio_alquiler = inicio_alquiler
                tiempo_alquiler = (datetime.now() - inicio_alquiler).total_seconds() / 3600
                if tiempo_alquiler <= 0.5:
                    return "El servicio ha sido gratis."
                else:
                    silla.devolver()
                    costo = self.calcular_tarifa(tiempo_alquiler)
                    self.transacciones.append((usuario, silla, inicio_alquiler, datetime.now(), costo))
                    return f"La tarifa a cobrar es de: ${costo}"

        return "No se pudo devolver la silla."

    def calcular_tarifa(self, tiempo_alquiler):
        tarifa_hora = 2.0
        tiempo_gratis = 0.5
        if tiempo_alquiler <= tiempo_gratis:
            return 0
        else:
            tiempo_cobrar = tiempo_alquiler - tiempo_gratis
            tarifa_total = tiempo_cobrar * tarifa_hora
            return tarifa_total
           