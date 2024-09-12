from src.services.periodo_service import crear_periodo, leer_periodos, actualizar_periodo, eliminar_periodo
from src.services.nivel_service import crear_nivel, leer_niveles, actualizar_nivel, eliminar_nivel
from src.services.asignatura_service import crear_asignatura, leer_asignaturas, actualizar_asignatura, eliminar_asignatura
from src.services.profesor_service import crear_profesor, leer_profesores, actualizar_profesor, eliminar_profesor
from src.services.estudiante_service import crear_estudiante, leer_estudiantes, actualizar_estudiante, eliminar_estudiante
from src.services.nota_service import crear_nota, agregar_detalle_nota, leer_notas, eliminar_nota
from src.services.curso_service import crear_curso, leer_cursos, actualizar_cursos, eliminar_curso
from src.services.matricula_service import crear_matricula, agregar_detalle_matricula, leer_matricula, eliminar_matricula

def mostrar_menu():
    print("\n--- Menú Gestión Académica ---")
    print("1. Gestionar Periodos")
    print("2. Gestionar Niveles")
    print("3. Gestionar Asignaturas")
    print("4. Gestionar Profesores")
    print("5. Gestionar Estudiantes")
    print("6. Gestionar Notas")
    print("7. Gestionar Cursos")
    print("8. Gestionar Matriculas")
    print("9. Salir")

def submenu_periodos():
    print("\n--- Gestión de Periodos ---")
    print("1. Crear Periodo")
    print("2. Ver Periodos")
    print("3. Actualizar Periodo")
    print("4. Eliminar Periodo")
    print("5. Volver")

def submenu_niveles():
    print("\n--- Gestión de Niveles ---")
    print("1. Crear Nivel")
    print("2. Ver Niveles")
    print("3. Actualizar Nivel")
    print("4. Eliminar Nivel")
    print("5. Volver")

def submenu_asignaturas():
    print("\n--- Gestión de Asignaturas ---")
    print("1. Crear Asignatura")
    print("2. Ver Asignaturas")
    print("3. Actualizar Asignatura")
    print("4. Eliminar Asignatura")
    print("5. Volver")

def submenu_profesores():
    print("\n--- Gestión de Profesores ---")
    print("1. Crear Profesor")
    print("2. Ver Profesores")
    print("3. Actualizar Profesor")
    print("4. Eliminar Profesor")
    print("5. Volver")

def submenu_estudiantes():
    print("\n--- Gestión de Estudiantes ---")
    print("1. Crear Estudiante")
    print("2. Ver Estudiantes")
    print("3. Actualizar Estudiante")
    print("4. Eliminar Estudiante")
    print("5. Volver")

def submenu_notas():
    print("\n--- Gestión de Notas ---")
    print("1. Crear Nota")
    print("2. Ver Notas")
    print("3. Agregar Detalle a Nota")
    print("4. Eliminar Nota")
    print("5. Volver")
    
def submenu_cursos():
    print("\n--- Gestión de Cursos ---")
    print("1. Crear Curso")
    print("2. Ver Cursos")
    print("3. Actualizar Cursos")
    print("4. Eliminar Cursos")
    print("5. Volver")

def submenu_matriculas():
    print("\n--- Gestión de Matriculas ---")
    print("1. Crear Matriculas")
    print("2. Ver Matriculas")
    print("3. Agregar Detalle a Matricula")
    print("4. Eliminar Matriculas")
    print("5. Volver")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                submenu_periodos()
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    id = input("Ingrese el ID del periodo: ")
                    nombre = input("Ingrese el nombre del periodo: ")
                    crear_periodo(id, nombre)
                elif subopcion == "2":
                    periodos = leer_periodos()
                    for id, periodo in periodos.items():
                        print(f"ID: {id}, Nombre: {periodo['periodo']}, Estado: {'Activo' if periodo['active'] else 'Inactivo'}")
                elif subopcion == "3":
                    id = input("Ingrese el ID del periodo a actualizar: ")
                    nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                    nuevo_estado = input("Nuevo estado (True/False o dejar vacío): ")
                    nuevo_estado = None if nuevo_estado == "" else nuevo_estado == "True"
                    actualizar_periodo(id, nuevo_nombre, nuevo_estado)
                elif subopcion == "4":
                    id = input("Ingrese el ID del periodo a eliminar: ")
                    eliminar_periodo(id)
                elif subopcion == "5":
                    break

        elif opcion == "2":
            while True:
                submenu_niveles()
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    id = input("Ingrese el ID del nivel: ")
                    nombre = input("Ingrese el nombre del nivel: ")
                    crear_nivel(id, nombre)
                elif subopcion == "2":
                    niveles = leer_niveles()
                    for id, nivel in niveles.items():
                        print(f"ID: {id}, Nivel: {nivel['nivel']}, Estado: {'Activo' if nivel['active'] else 'Inactivo'}")
                elif subopcion == "3":
                    id = input("Ingrese el ID del nivel a actualizar: ")
                    nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                    nuevo_estado = input("Nuevo estado (True/False o dejar vacío): ")
                    nuevo_estado = None if nuevo_estado == "" else nuevo_estado == "True"
                    actualizar_nivel(id, nuevo_nombre, nuevo_estado)
                elif subopcion == "4":
                    id = input("Ingrese el ID del nivel a eliminar: ")
                    eliminar_nivel(id)
                elif subopcion == "5":
                    break

        elif opcion == "3":
            while True:
                submenu_asignaturas()
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    id = input("Ingrese el ID de la asignatura: ")
                    descripcion = input("Ingrese la descripción de la asignatura: ")
                    nivel = input("Ingrese el nivel de la asignatura: ")
                    crear_asignatura(id, descripcion, nivel)
                elif subopcion == "2":
                    asignaturas = leer_asignaturas()
                    for id, asignatura in asignaturas.items():
                        print(f"ID: {id}, Descripción: {asignatura['descripcion']}, Nivel: {asignatura['nivel']}, Estado: {'Activo' if asignatura['active'] else 'Inactivo'}")
                elif subopcion == "3":
                    id = input("Ingrese el ID de la asignatura a actualizar: ")
                    nueva_descripcion = input("Nueva descripción (dejar vacío para no cambiar): ")
                    nuevo_estado = input("Nuevo estado (True/False o dejar vacío): ")
                    nuevo_estado = None if nuevo_estado == "" else nuevo_estado == "True"
                    actualizar_asignatura(id, nueva_descripcion, nuevo_estado)
                elif subopcion == "4":
                    id = input("Ingrese el ID de la asignatura a eliminar: ")
                    eliminar_asignatura(id)
                elif subopcion == "5":
                    break

        elif opcion == "4":
            while True:
                submenu_profesores()
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    id = input("Ingrese el ID del profesor: ")
                    nombre = input("Ingrese el nombre del profesor: ")
                    crear_profesor(id, nombre)
                elif subopcion == "2":
                    profesores = leer_profesores()
                    for id, profesor in profesores.items():
                        print(f"ID: {id}, Nombre: {profesor['nombre']}, Estado: {'Activo' if profesor['active'] else 'Inactivo'}")
                elif subopcion == "3":
                    id = input("Ingrese el ID del profesor a actualizar: ")
                    nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                    nuevo_estado = input("Nuevo estado (True/False o dejar vacío): ")
                    nuevo_estado = None if nuevo_estado == "" else nuevo_estado == "True"
                    actualizar_profesor(id, nuevo_nombre, nuevo_estado)
                elif subopcion == "4":
                    id = input("Ingrese el ID del profesor a eliminar: ")
                    eliminar_profesor(id)
                elif subopcion == "5":
                    break

        elif opcion == "5":
            while True:
                submenu_estudiantes()
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    id = input("Ingrese el ID del estudiante: ")
                    nombre = input("Ingrese el nombre del estudiante: ")
                    crear_estudiante(id, nombre)
                elif subopcion == "2":
                    estudiantes = leer_estudiantes()
                    for id, estudiante in estudiantes.items():
                        print(f"ID: {id}, Nombre: {estudiante['nombre']}, Estado: {'Activo' if estudiante['active'] else 'Inactivo'}")
                elif subopcion == "3":
                    id = input("Ingrese el ID del estudiante a actualizar: ")
                    nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                    nuevo_estado = input("Nuevo estado (True/False o dejar vacío): ")
                    nuevo_estado = None if nuevo_estado == "" else nuevo_estado == "True"
                    actualizar_estudiante(id, nuevo_nombre, nuevo_estado)
                elif subopcion == "4":
                    id = input("Ingrese el ID del estudiante a eliminar: ")
                    eliminar_estudiante(id)
                elif subopcion == "5":
                    break

        elif opcion == "6":
            while True:
                submenu_notas()
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    id = input("Ingrese el ID de la nota: ")
                    periodo = input("Ingrese el ID del periodo: ")
                    profesor = input("Ingrese el ID del profesor: ")
                    asignatura = input("Ingrese el ID de la asignatura: ")
                    crear_nota(id, periodo, profesor, asignatura)
                elif subopcion == "2":
                    notas = leer_notas()
                    for id, nota in notas.items():
                        print(f"ID: {id}, Periodo: {nota['periodo']}, Profesor: {nota['profesor']}, Asignatura: {nota['asignatura']}, Estado: {'Activo' if nota['active'] else 'Inactivo'}")
                        print("Detalles de Notas:")
                        for detalle in nota['detalleNota']:
                            print(f"  - Estudiante: {detalle['estudiante']}, Nota1: {detalle['nota1']}, Nota2: {detalle['nota2']}, Recuperación: {detalle['recuperacion']}, Observación: {detalle['observacion']}")
                elif subopcion == "3":
                    id_nota = input("Ingrese el ID de la nota: ")
                    id_detalle = input("Ingrese el ID del detalle: ")
                    estudiante = input("Ingrese el ID del estudiante: ")
                    nota1 = float(input("Ingrese la nota 1: "))
                    nota2 = float(input("Ingrese la nota 2: "))
                    recuperacion = input("Ingrese la nota de recuperación (opcional): ")
                    observacion = input("Ingrese una observación (opcional): ")
                    agregar_detalle_nota(id_nota, id_detalle, estudiante, nota1, nota2, recuperacion, observacion)
                elif subopcion == "4":
                    id = input("Ingrese el ID de la nota a eliminar: ")
                    eliminar_nota(id)
                elif subopcion == "5":
                    break
        
        elif opcion == "7":
            while True:
                submenu_cursos()
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    id = input("Ingrese el ID del curso: ")
                    descripcion = input("Ingrese la descripción del curso: ")
                    nivel = input("Ingrese el nivel del curso: ")
                    crear_curso(id, descripcion, nivel)
                elif subopcion == "2":
                    cursos = leer_cursos()
                    for id, cursos in cursos.items():
                        print(f"ID: {id}, Descripción: {cursos['descripcion']}, Nivel: {cursos['nivel']}, Estado: {'Activo' if cursos['active'] else 'Inactivo'}")
                elif subopcion == "3":
                    id = input("Ingrese el ID del curso a actualizar: ")
                    nueva_descripcion = input("Nueva descripción (dejar vacío para no cambiar): ")
                    nuevo_estado = input("Nuevo estado (True/False o dejar vacío): ")
                    nuevo_estado = None if nuevo_estado == "" else nuevo_estado == "True"
                    actualizar_cursos(id, nueva_descripcion, nuevo_estado)
                elif subopcion == "4":
                    id = input("Ingrese el ID del curso a eliminar: ")
                    eliminar_curso(id)
                elif subopcion == "5":
                    break
        
        elif opcion == "8":
            while True:
                submenu_matriculas()
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    id = input("Ingrese el ID de la matricula: ")
                    periodo = input("Ingrese el ID del periodo: ")
                    estudiante = input("Ingrese el ID del estudiante: ")
                    crear_matricula(id, periodo, estudiante)
                elif subopcion == "2":
                    matriculas = leer_matricula()
                    for id, matriculas in matriculas.items():
                        print(f"ID: {id}, Periodo: {nota['periodo']},  Estudiante: {nota['estudiante']}, Estado: {'Activo' if nota['active'] else 'Inactivo'}")
                        print("Detalles de Matriculas:")
                        for detalle in matriculas['detalleMatricula']:
                            print(f"  - Asignatura: {detalle['asignatura']}, Profesor: {detalle['profesor']}, Curso: {detalle['curso']}")
                elif subopcion == "3":
                    id_matricula = input("Ingrese el ID de la matricula: ")
                    id_detalle = input("Ingrese el ID del detalle: ")
                    estudiante = input("Ingrese el ID del asignatura: ")
                    profesor = float(input("Ingrese el profesor: "))
                    curso = float(input("Ingrese el curso: "))
                    agregar_detalle_matricula(id_matricula, id_detalle, asignatura, profesor, curso)
                elif subopcion == "4":
                    id = input("Ingrese el ID de la matricula a eliminar: ")
                    eliminar_matricula(id)
                elif subopcion == "5":
                    break       

        elif opcion == "9":
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()