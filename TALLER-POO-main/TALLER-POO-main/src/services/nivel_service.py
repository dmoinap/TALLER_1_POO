import json
from os.path import exists
from src.models.nivel import Nivel
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'niveles.json')

def cargar_niveles():
    if exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def guardar_niveles(niveles):
    with open(FILE_PATH, 'w') as file:
        json.dump(niveles, file, indent=4)

def crear_nivel(id, nivel, active=True):
    niveles = cargar_niveles()
    niveles[id] = {
        "id": id,
        "nivel": nivel,
        "fecha_creacion": str(Nivel(id, nivel).fecha_creacion),
        "active": active
    }
    guardar_niveles(niveles)
    print(f"Nivel {nivel} creado exitosamente.")

def leer_niveles():
    return cargar_niveles()

def actualizar_nivel(id, nuevo_nivel=None, nuevo_estado=None):
    niveles = cargar_niveles()
    if id in niveles:
        if nuevo_nivel:
            niveles[id]['nivel'] = nuevo_nivel
        if nuevo_estado is not None:
            niveles[id]['active'] = nuevo_estado
        guardar_niveles(niveles)
        print(f"Nivel {id} actualizado.")
    else:
        print(f"Nivel {id} no encontrado.")

def eliminar_nivel(id):
    niveles = cargar_niveles()
    if id in niveles:
        del niveles[id]
        guardar_niveles(niveles)
        print(f"Nivel {id} eliminado.")
    else:
        print(f"Nivel {id} no encontrado.")
