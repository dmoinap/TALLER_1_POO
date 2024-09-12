import json
from os.path import exists
from src.models.matricula import Matricula, DetalleMatricula
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'matriculas.json')

def cargar_matriculas():
    if exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def guardar_matriculas(matriculas):
    with open(FILE_PATH, 'w') as file:
        json.dump(matriculas, file, indent=4)

def crear_matricula(id, periodo, estudiante, active=True):
    matriculas = cargar_matriculas()
    matriculas[id] = {
        "id": id,
        "periodo": periodo,
        "estudiante": estudiante,
        "detalleMatricula": [],
        "fecha_creacion": str(Matricula(id, periodo, estudiante).fecha_creacion),
        "active": active
    }
    guardar_matriculas(matriculas)
    print(f"Nota para la matricula {matriculas} creada exitosamente.")

def leer_matricula():
    return cargar_matriculas()

def agregar_detalle_matricula(id_matricula, id_detalle, asignatura, profesor, curso):
    matriculas = cargar_matriculas()
    if id_matricula in matriculas:
        detalle = {
            "id": id_detalle,
            "asignatura": asignatura,
            "profesor": profesor,
            "curso": curso,
        }
        matriculas[id_matricula]['detalleMatricula'].append(detalle)
        guardar_matriculas(matriculas)
        print(f"Detalle de matricula agregado exitosamente a la matricula {id_matricula}.")
    else:
        print(f"Matricula {id_matricula} no encontrada.")

def eliminar_matricula(id):
    matriculas = cargar_matriculas()
    if id in matriculas:
        del matriculas[id]
        guardar_matriculas(matriculas)
        print(f"Matricula {id} eliminada.")
    else:
        print(f"Matricula {id} no encontrada.")
