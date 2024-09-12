from datetime import date

class Nivel:
    def __init__(self, id, nivel, active=True):
        self.id = id
        self.nivel = nivel
        self.fecha_creacion = str(date.today())
        self.active = active
