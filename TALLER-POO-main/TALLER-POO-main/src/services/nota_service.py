import json
from os.path import exists
from src.models.nota import Nota, DetalleNota
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'notas.json')

def cargar_notas():
    if exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def guardar_notas(notas):
    with open(FILE_PATH, 'w') as file:
        json.dump(notas, file, indent=4)

def crear_nota(id, periodo, profesor, asignatura, active=True):
    notas = cargar_notas()
    notas[id] = {
        "id": id,
        "periodo": periodo,
        "profesor": profesor,
        "asignatura": asignatura,
        "detalleNota": [],
        "fecha_creacion": str(Nota(id, periodo, profesor, asignatura).fecha_creacion),
        "active": active
    }
    guardar_notas(notas)
    print(f"Nota para la asignatura {asignatura} creada exitosamente.")

def leer_notas():
    return cargar_notas()

def agregar_detalle_nota(id_nota, id_detalle, estudiante, nota1, nota2, recuperacion=None, observacion=None):
    notas = cargar_notas()
    if id_nota in notas:
        detalle = {
            "id": id_detalle,
            "estudiante": estudiante,
            "nota1": nota1,
            "nota2": nota2,
            "recuperacion": recuperacion,
            "observacion": observacion
        }
        notas[id_nota]['detalleNota'].append(detalle)
        guardar_notas(notas)
        print(f"Detalle de nota agregado exitosamente a la nota {id_nota}.")
    else:
        print(f"Nota {id_nota} no encontrada.")

def eliminar_nota(id):
    notas = cargar_notas()
    if id in notas:
        del notas[id]
        guardar_notas(notas)
        print(f"Nota {id} eliminada.")
    else:
        print(f"Nota {id} no encontrada.")
import json
from os.path import exists
from src.models.nota import Nota, DetalleNota
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'notas.json')

def cargar_notas():
    if exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def guardar_notas(notas):
    with open(FILE_PATH, 'w') as file:
        json.dump(notas, file, indent=4)

def crear_nota(id, periodo, profesor, asignatura, active=True):
    notas = cargar_notas()
    notas[id] = {
        "id": id,
        "periodo": periodo,
        "profesor": profesor,
        "asignatura": asignatura,
        "detalleNota": [],
        "fecha_creacion": str(Nota(id, periodo, profesor, asignatura).fecha_creacion),
        "active": active
    }
    guardar_notas(notas)
    print(f"Nota para la asignatura {asignatura} creada exitosamente.")

def leer_notas():
    return cargar_notas()

def agregar_detalle_nota(id_nota, id_detalle, estudiante, nota1, nota2, recuperacion=None, observacion=None):
    notas = cargar_notas()
    if id_nota in notas:
        detalle = {
            "id": id_detalle,
            "estudiante": estudiante,
            "nota1": nota1,
            "nota2": nota2,
            "recuperacion": recuperacion,
            "observacion": observacion
        }
        notas[id_nota]['detalleNota'].append(detalle)
        guardar_notas(notas)
        print(f"Detalle de nota agregado exitosamente a la nota {id_nota}.")
    else:
        print(f"Nota {id_nota} no encontrada.")

def eliminar_nota(id):
    notas = cargar_notas()
    if id in notas:
        del notas[id]
        guardar_notas(notas)
        print(f"Nota {id} eliminada.")
    else:
        print(f"Nota {id} no encontrada.")
