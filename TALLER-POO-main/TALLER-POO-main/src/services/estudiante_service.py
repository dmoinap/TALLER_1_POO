import json
from os.path import exists
from src.models.estudiante import Estudiante
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'estudiantes.json')

def cargar_estudiantes():
    if exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def guardar_estudiantes(estudiantes):
    with open(FILE_PATH, 'w') as file:
        json.dump(estudiantes, file, indent=4)

def crear_estudiante(id, nombre, active=True):
    estudiantes = cargar_estudiantes()
    estudiantes[id] = {
        "id": id,
        "nombre": nombre,
        "fecha_creacion": str(Estudiante(id, nombre).fecha_creacion),
        "active": active
    }
    guardar_estudiantes(estudiantes)
    print(f"Estudiante {nombre} creado exitosamente.")

def leer_estudiantes():
    return cargar_estudiantes()

def actualizar_estudiante(id, nuevo_nombre=None, nuevo_estado=None):
    estudiantes = cargar_estudiantes()
    if id in estudiantes:
        if nuevo_nombre:
            estudiantes[id]['nombre'] = nuevo_nombre
        if nuevo_estado is not None:
            estudiantes[id]['active'] = nuevo_estado
        guardar_estudiantes(estudiantes)
        print(f"Estudiante {id} actualizado.")
    else:
        print(f"Estudiante {id} no encontrado.")

def eliminar_estudiante(id):
    estudiantes = cargar_estudiantes()
    if id in estudiantes:
        del estudiantes[id]
        guardar_estudiantes(estudiantes)
        print(f"Estudiante {id} eliminado.")
    else:
        print(f"Estudiante {id} no encontrado.")
