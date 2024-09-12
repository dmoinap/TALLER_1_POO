from datetime import date

class Periodo:
    def __init__(self, id, periodo, active=True):
        self.id = id
        self.periodo = periodo
        self.fecha_creacion = str(date.today())
        self.active = active
