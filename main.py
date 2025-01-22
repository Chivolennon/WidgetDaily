# "#" SE USA PARA COMENTAR COSAS. USAREMOS TAMBIÉN "tkinter" para crear luego la interfaz GUI.
# Windows ya lo tiene instalado.

print("Primera prueba para solución Widget Daily.")

# La solución tendrá como disposición :
# Agregar tareas, Listar tareas, Marcar tareas como completadas, Eliminar tareas.


# Lista donde se van a almacenar las tareas.

tareas = []

# Función para agregar una tarea.

def agregarTarea(nombre):
    nuevaTarea ={
        "id": len(tareas) + 1,
        "nombre": nombre,
        "completada": False
    }
    tareas.append(nuevaTarea)
    print(f"Tarea '{nombre}' agregada.")

# Función para enlistar las tareas.

def listarTareas():
    print("\nLista de Tareas:")
    for tarea in tareas:
        estado = "[X]" if tarea["completada"] else "[]"
        print(f"{tarea['id']}. {tarea['nombre']} - {estado}")
    print()

# Función para eliminar una tarea.

def eliminarTarea(idTarea):
    global tareas
    tareas = [tarea for tarea in tareas if tarea["id"] != idTarea]
    print(f"Tarea con el ID {idTarea} a sido eliminada.")

# Función para completar una tarea.
def  completarTarea(idTarea):
    for tarea in tareas:
        if tarea["id"] == idTarea:
            tarea["completada"] = True
            print(f"Tarea '{tarea['nombre']}' completada. ")
            return
    print(f"Tarea con ID {idTarea} no encontrada.")


# Pruebas

if __name__ == "__main__":
    agregarTarea("Estudiar Python")
    agregarTarea("No hacer nada")
    listarTareas()
    completarTarea(1)
    listarTareas()
    eliminarTarea(2)
    listarTareas()