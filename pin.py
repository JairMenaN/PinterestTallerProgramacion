# actualizacion_pin.py
# Datos de ejemplo para pins
pins = {
    1: {"titulo": "Receta de pastel de manzana", "url": "https://pinpastel.com/pastel", "descripcion": "Una receta fácil para un delicioso pastel de manzana"},
    2: {"titulo": "Proyecto de lámpara reciclada", "url": "https://pinlamp.com/lamp", "descripcion": "Lámpara con materiales reciclados"}
}

# Función para actualizar un pin
def actualizar_pin():
    pin_id = int(input("Ingrese el ID del pin que desea actualizar: "))
    if pin_id in pins:
        nuevo_titulo = input("Ingrese el nuevo título del pin (deje vacío para no cambiar): ")
        nueva_url = input("Ingrese la nueva URL del contenido (deje vacío para no cambiar): ")
        nueva_descripcion = input("Ingrese la nueva descripción del pin (deje vacío para no cambiar): ")

        if nuevo_titulo:
            pins[pin_id]["titulo"] = nuevo_titulo
        if nueva_url:
            pins[pin_id]["url"] = nueva_url
        if nueva_descripcion:
            pins[pin_id]["descripcion"] = nueva_descripcion

        print(f"El pin con ID {pin_id} ha sido actualizado:")
        print(f"Título: {pins[pin_id]['titulo']}")
        print(f"URL: {pins[pin_id]['url']}")
        print(f"Descripción: {pins[pin_id]['descripcion']}")
    else:
        print("ID de pin no válido.")

# Llamada a la función para probar
if __name__ == "__main__":
    actualizar_pin()
