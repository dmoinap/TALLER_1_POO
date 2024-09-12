import json
from os.path import exists
from src.models.profesor import Profesor
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'profesores.json')

def cargar_profesores():
    if exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def guardar_profesores(profesores):
    with open(FILE_PATH, 'w') as file:
        json.dump(profesores, file, indent=4)

def crear_profesor(id, nombre, active=True):
    profesores = cargar_profesores()
    profesores[id] = {
        "id": id,
        "nombre": nombre,
        "fecha_creacion": str(Profesor(id, nombre).fecha_creacion),
        "active": active
    }
    guardar_profesores(profesores)
    print(f"Profesor {nombre} creado exitosamente.")

def leer_profesores():
    return cargar_profesores()

def actualizar_profesor(id, nuevo_nombre=None, nuevo_estado=None):
    profesores = cargar_profesores()
    if id in profesores:
        if nuevo_nombre:
            profesores[id]['nombre'] = nuevo_nombre
        if nuevo_estado is not None:
            profesores[id]['active'] = nuevo_estado
        guardar_profesores(profesores)
        print(f"Profesor {id} actualizado.")
    else:
        print(f"Profesor {id} no encontrado.")

def eliminar_profesor(id):
    profesores = cargar_profesores()
    if id in profesores:
        del profesores[id]
        guardar_profesores(profesores)
        print(f"Profesor {id} eliminado.")
    else:
        print(f"Profesor {id} no encontrado.")
