class Tarifas:
    def __init__(self):
        self.tarifas = {}

    def agregar_tarifa(self, numero_serie, tarifa_por_hora):
        self.tarifas[numero_serie] = tarifa_por_hora

    def obtener_tarifa(self, numero_serie):
        return self.tarifas.get(numero_serie, 0)