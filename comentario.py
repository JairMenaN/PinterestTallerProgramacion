# Datos de ejemplo para comentarios con diferentes números
comentarios = {
    1: {1: "¡Me encanta esta receta! Muy fácil de seguir."},
    2: {2: "Gran idea, me gustaría hacer algo similar."}
}

# Función para actualizar un comentario
def actualizar_comentario():
    pin_id = int(input("Ingrese el ID del pin donde se encuentra el comentario: "))
    if pin_id in comentarios:
        comentario_id = int(input("Ingrese el ID del comentario que desea actualizar: "))
        if comentario_id in comentarios[pin_id]:
            nuevo_comentario = input("Ingrese el nuevo contenido del comentario: ")
            comentarios[pin_id][comentario_id] = nuevo_comentario
            print(f"El comentario con ID {comentario_id} en el pin {pin_id} ha sido actualizado:")
            print(f"Nuevo comentario: {nuevo_comentario}")
        else:
            print("ID de comentario no válido.")
    else:
        print("ID de pin no válido.")

# Llamada a la función para probar
if __name__ == "__main__":
    actualizar_comentario()
