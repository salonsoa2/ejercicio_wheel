class Wheel:
    def __init__(self, ancho, rodadura, diametro):
        self.mm = ancho
        self.rod = rodadura
        self.pulgadas = diametro
        self.presion = 0
    def set_pressure(self, presion):
        self.presion = presion
    def print_info(self, prin):
        self.prin = prin


