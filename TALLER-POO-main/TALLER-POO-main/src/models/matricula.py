from datetime import date

class Matricula:
    def __init__(self, id, periodo, estudiante, active=True):
        self.id = id
        self.periodo = periodo
        self.estudiante = estudiante 
        self.detalleMatricula = []
        self.fecha_creacion = str(date.today())
        self.active = active

    def addMatricula(self, detalle_matricula):
        self.detalleMatricula.append(detalle_matricula)

class DetalleMatricula:
    def __init__(self, id, asignatura, profesor, curso):
        self.id = id
        self.asignatura = asignatura
        self.profesor = profesor
        self.curso = curso