import questionary
from tareas import cargar_tareas, guardar_tareas, agregar_tarea, listar_tareas, completar_tarea, eliminar_tarea


#Este es el main del codigo as
def main():
    tareas = cargar_tareas()

    while True:
        opcion = questionary.select(
            "¿Qué deseas hacer?",
            choices=[
                "Agregar tarea",
                "Listar tareas",
                "Completar tarea",
                "Eliminar tarea",
                "Salir"
            ]).ask()

        if opcion == "Agregar tarea":
            descripcion = questionary.text("Descripción de la tarea:").ask()
            prioridad = questionary.select("Prioridad:", choices=["Alta", "Media", "Baja"]).ask()
            agregar_tarea(tareas, descripcion, prioridad)
        elif opcion == "Listar tareas":
            listar_tareas(tareas)
        elif opcion == "Completar tarea":
            completar_tarea(tareas)
        elif opcion == "Eliminar tarea":
            eliminar_tarea(tareas)
        elif opcion == "Salir":
            break

        guardar_tareas(tareas)

if __name__ == "__main__":
    main()
