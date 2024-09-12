import json
from os.path import exists
from src.models.periodo import Periodo
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'periodos.json')

def cargar_periodos():
    if exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def guardar_periodos(periodos):
    with open(FILE_PATH, 'w') as file:
        json.dump(periodos, file, indent=4)

def crear_periodo(id, periodo, active=True):
    periodos = cargar_periodos()
    periodos[id] = {
        "id": id,
        "periodo": periodo,
        "fecha_creacion": str(Periodo(id, periodo).fecha_creacion),
        "active": active
    }
    guardar_periodos(periodos)
    print(f"Periodo {periodo} creado exitosamente.")

def leer_periodos():
    return cargar_periodos()

def actualizar_periodo(id, nuevo_periodo=None, nuevo_estado=None):
    periodos = cargar_periodos()
    if id in periodos:
        if nuevo_periodo:
            periodos[id]['periodo'] = nuevo_periodo
        if nuevo_estado is not None:
            periodos[id]['active'] = nuevo_estado
        guardar_periodos(periodos)
        print(f"Periodo {id} actualizado.")
    else:
        print(f"Periodo {id} no encontrado.")

def eliminar_periodo(id):
    periodos = cargar_periodos()
    if id in periodos:
        del periodos[id]
        guardar_periodos(periodos)
        print(f"Periodo {id} eliminado.")
    else:
        print(f"Periodo {id} no encontrado.")
