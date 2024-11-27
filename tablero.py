# actualizacion_tablero.py

# Datos de ejemplo para tableros
tableros = {
    1: {"nombre": "Tablero de recetas", "descripcion": "Tablero con recetas deliciosas"},
    2: {"nombre": "Tablero de DIY", "descripcion": "Proyectos de bricolaje y manualidades"}
}

# Función para actualizar un tablero
def actualizar_tablero():
    tablero_id = int(input("Ingrese el ID del tablero que desea actualizar: "))
    if tablero_id in tableros:
        nuevo_nombre = input("Ingrese el nuevo nombre del tablero (deje vacío para no cambiar): ")
        nueva_descripcion = input("Ingrese la nueva descripción del tablero (deje vacío para no cambiar): ")

        if nuevo_nombre:
            tableros[tablero_id]["nombre"] = nuevo_nombre
        if nueva_descripcion:
            tableros[tablero_id]["descripcion"] = nueva_descripcion

        print(f"El tablero con ID {tablero_id} ha sido actualizado:")
        print(f"Nombre: {tableros[tablero_id]['nombre']}")
        print(f"Descripción: {tableros[tablero_id]['descripcion']}")
    else:
        print("ID de tablero no válido.")

# Llamada a la función para probar
if __name__ == "__main__":
    actualizar_tablero()
