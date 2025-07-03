import csv

def cargar_tareas():
    tareas = []
    try:
        with open("tareas.csv", newline="") as f:
            reader = csv.DictReader(f)
            tareas = list(reader)
    except FileNotFoundError:
        pass
    return tareas

def guardar_tareas(tareas):
    with open("tareas.csv", "w", newline="") as f:
        fieldnames = ["descripcion", "prioridad", "completada"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tarea in tareas:
            writer.writerow(tarea)

def agregar_tarea(tareas, descripcion, prioridad):
    tareas.append({"descripcion": descripcion, "prioridad": prioridad, "completada": "No"})

def listar_tareas(tareas):
    for i, tarea in enumerate(tareas):
        estado = "✅" if tarea["completada"] == "Sí" else "❌"
        print(f"{i+1}. [{estado}] {tarea['descripcion']} ({tarea['prioridad']})")

def completar_tarea(tareas):
    listar_tareas(tareas)
    num = int(input("Número de la tarea a completar: ")) - 1
    if 0 <= num < len(tareas):
        tareas[num]["completada"] = "Sí"

def eliminar_tarea(tareas):
    listar_tareas(tareas)
    num = int(input("Número de la tarea a eliminar: ")) - 1
    if 0 <= num < len(tareas):
        tareas.pop(num)
