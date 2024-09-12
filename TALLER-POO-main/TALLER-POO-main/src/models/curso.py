from datetime import date

class Curso:
    def __init__(self, id, descripcion, nivel, active=True):
        self.id = id
        self.descripcion = descripcion
        self.nivel = nivel
        self.fecha_creacion = str(date.today())
        self.active = active
    