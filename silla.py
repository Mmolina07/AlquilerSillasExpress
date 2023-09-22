from silla import Silla
from usuario import Usuario
from tarifas import Tarifas
from sistemaalquiler import SistemaAlquiler
class Silla:
    def __init__(self, numero_serie, modelo):
        self.numero_serie = numero_serie
        self.modelo = modelo
        self.disponible = True

    def alquilar(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True
