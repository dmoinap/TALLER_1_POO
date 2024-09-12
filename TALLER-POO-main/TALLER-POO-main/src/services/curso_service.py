import json
from os.path import exists
from src.models.curso import Curso
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'cursos.json')

def cargar_cursos():
    if exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def guardar_cursos(cursos):
    with open(FILE_PATH, 'w') as file:
        json.dump(cursos, file, indent=4)

def crear_curso(id, descripcion, nivel, active=True):
    cursos = cargar_cursos()
    cursos[id] = {
        "id": id,
        "descripcion": descripcion,
        "nivel": nivel,
        "fecha_creacion": str(Curso(id, descripcion, nivel).fecha_creacion),
        "active": active
    }
    guardar_cursos(cursos)
    print(f"Curso {descripcion} creada exitosamente.")

def leer_cursos():
    return cargar_cursos()

def actualizar_cursos(id, nueva_descripcion=None, nuevo_estado=None):
    cursos = cargar_cursos()
    if id in cursos:
        if nueva_descripcion:
            cursos[id]['descripcion'] = nueva_descripcion
        if nuevo_estado is not None:
            cursos[id]['active'] = nuevo_estado
        guardar_cursos(cursos)
        print(f"Curso {id} actualizada.")
    else:
        print(f"Curso {id} no encontrada.")

def eliminar_curso(id):
    cursos = cargar_cursos()
    if id in cursos:
        del cursos[id]
        guardar_cursos(cursos)
        print(f"Curso {id} eliminada.")
    else:
        print(f"Curso {id} no encontrada.")
