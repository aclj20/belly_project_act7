# src/belly.py
from src.clock import get_current_time

class Belly:
    def __init__(self, clock_service=None):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0
        self.clock_service = clock_service or get_current_time

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        print(f"He comido {pepinos} pepinos.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def gruñir_condiciones(self):
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10

    def esta_gruñendo(self):
        return self.gruñir_condiciones()
    
    def pepinos_ingestados(self):
        return self.pepinos_comidos
