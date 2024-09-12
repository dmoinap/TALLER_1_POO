from datetime import date

class Estudiante:
    def __init__(self, id, nombre, active=True):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = str(date.today())
        self.active = active
