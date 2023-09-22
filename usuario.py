from silla import Silla
from usuario import Usuario
from tarifas import Tarifas
from sistemaalquiler import SistemaAlquiler
class Usuario:
    def __init__(self, nombre, correo, identificacion):
        self.nombre = nombre
        self.correo = correo
        self.identificacion = identificacion