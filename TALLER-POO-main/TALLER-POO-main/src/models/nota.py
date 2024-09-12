from datetime import date

class Nota:
    def __init__(self, id, periodo, profesor, asignatura, active=True):
        self.id = id
        self.periodo = periodo
        self.profesor = profesor
        self.asignatura = asignatura
        self.detalleNota = []
        self.fecha_creacion = str(date.today())
        self.active = active

    def addNota(self, detalle_nota):
        self.detalleNota.append(detalle_nota)

class DetalleNota:
    def __init__(self, id, estudiante, nota1, nota2, recuperacion=None, observacion=None):
        self.id = id
        self.estudiante = estudiante
        self.nota1 = nota1
        self.nota2 = nota2
        self.recuperacion = recuperacion
        self.observacion = observacion
