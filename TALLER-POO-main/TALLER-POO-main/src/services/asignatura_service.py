import json
from os.path import exists
from src.models.asignatura import Asignatura
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'asignaturas.json')

def cargar_asignaturas():
    if exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def guardar_asignaturas(asignaturas):
    with open(FILE_PATH, 'w') as file:
        json.dump(asignaturas, file, indent=4)

def crear_asignatura(id, descripcion, nivel, active=True):
    asignaturas = cargar_asignaturas()
    asignaturas[id] = {
        "id": id,
        "descripcion": descripcion,
        "nivel": nivel,
        "fecha_creacion": str(Asignatura(id, descripcion, nivel).fecha_creacion),
        "active": active
    }
    guardar_asignaturas(asignaturas)
    print(f"Asignatura {descripcion} creada exitosamente.")

def leer_asignaturas():
    return cargar_asignaturas()

def actualizar_asignatura(id, nueva_descripcion=None, nuevo_estado=None):
    asignaturas = cargar_asignaturas()
    if id in asignaturas:
        if nueva_descripcion:
            asignaturas[id]['descripcion'] = nueva_descripcion
        if nuevo_estado is not None:
            asignaturas[id]['active'] = nuevo_estado
        guardar_asignaturas(asignaturas)
        print(f"Asignatura {id} actualizada.")
    else:
        print(f"Asignatura {id} no encontrada.")

def eliminar_asignatura(id):
    asignaturas = cargar_asignaturas()
    if id in asignaturas:
        del asignaturas[id]
        guardar_asignaturas(asignaturas)
        print(f"Asignatura {id} eliminada.")
    else:
        print(f"Asignatura {id} no encontrada.")
