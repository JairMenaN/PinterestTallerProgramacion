class Usuario:
    usuarios = {}

    def __init__(self, nombre, correo, contraseña, descripcion=None, imagen=None):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.descripcion = descripcion
        self.imagen = imagen

    @classmethod
    def crear_usuario(cls):
        print("=== Crear Nuevo Usuario ===")
        nombre = input("Nombre completo: ").strip()
        correo = input("Dirección de correo electrónico: ").strip()
        contraseña = input("Contraseña: ").strip()

        # Validaciones de campos obligatorios
        if not nombre or not correo or not contraseña:
            print("Error: Los campos 'Nombre', 'Correo' y 'Contraseña' son obligatorios.")
            return

        if correo in cls.usuarios:
            print("Error: El correo electrónico ya está registrado.")
            return

        descripcion = input("Descripción personal (opcional): ").strip()
        imagen = input("Ruta de la imagen de perfil (opcional): ").strip()

        cls.usuarios[correo] = Usuario(nombre, correo, contraseña, descripcion, imagen)
        print(f"Usuario '{nombre}' creado exitosamente. ¡Bienvenido a Pinterest!")

class Tablero:
    tableros = {}
    id_counter = 1

    def __init__(self, nombre, descripcion, creador):
        self.id = Tablero.id_counter
        self.nombre = nombre
        self.descripcion = descripcion
        self.creador = creador
        Tablero.id_counter += 1

    @classmethod
    def crear_tablero(cls):
        print("=== Crear Nuevo Tablero ===")
        nombre_tablero = input("Nombre del tablero: ").strip()
        descripcion = input("Descripción del tablero: ").strip()
        creador = input("Nombre del usuario: ").strip()

        # Validación de usuario existente
        if creador not in [usuario.nombre for usuario in Usuario.usuarios.values()]:
            print("Error: Usuario no encontrado. Registre un usuario primero.")
            return

        # Validación de campos obligatorios
        if not nombre_tablero or not descripcion:
            print("Error: Los campos 'Nombre del tablero' y 'Descripción' son obligatorios.")
            return

        tablero = Tablero(nombre_tablero, descripcion, creador)
        cls.tableros[tablero.id] = tablero
        print(f"Tablero '{nombre_tablero}' creado exitosamente por {creador}.")

class Pin:
    pins = {}
    id_counter = 1

    def __init__(self, titulo, url, descripcion, tablero_id, creador):
        self.id = Pin.id_counter
        self.titulo = titulo
        self.url = url
        self.descripcion = descripcion
        self.tablero_id = tablero_id
        self.creador = creador
        Pin.id_counter += 1

    @classmethod
    def agregar_pin(cls):
        print("=== Agregar Nuevo Pin ===")
        tablero_id = input("ID del tablero: ").strip()
        
        if not tablero_id.isdigit() or int(tablero_id) not in Tablero.tableros:
            print("Error: Tablero no encontrado o ID inválido.")
            return
        
        tablero_id = int(tablero_id)
        titulo = input("Título del pin: ").strip()
        url = input("URL del contenido: ").strip()
        descripcion = input("Descripción del pin: ").strip()
        creador = input("Nombre del usuario: ").strip()

        # Validaciones
        if creador not in [usuario.nombre for usuario in Usuario.usuarios.values()]:
            print("Error: Usuario no encontrado. Registre un usuario primero.")
            return

        if not titulo or not url or not descripcion:
            print("Error: Los campos 'Título', 'URL' y 'Descripción' son obligatorios.")
            return

        pin = Pin(titulo, url, descripcion, tablero_id, creador)
        cls.pins[pin.id] = pin
        print(f"Pin '{titulo}' agregado exitosamente al tablero ID {tablero_id}.")

class Comentario:
    comentarios = {}
    id_counter = 1

    def __init__(self, pin_id, creador, contenido):
        self.id = Comentario.id_counter
        self.pin_id = pin_id
        self.creador = creador
        self.contenido = contenido
        Comentario.id_counter += 1

    @classmethod
    def agregar_comentario(cls):
        print("=== Agregar Comentario ===")
        pin_id = input("ID del pin: ").strip()
        
        if not pin_id.isdigit() or int(pin_id) not in Pin.pins:
            print("Error: Pin no encontrado o ID inválido.")
            return
        
        pin_id = int(pin_id)
        creador = input("Nombre del usuario: ").strip()
        contenido = input("Contenido del comentario: ").strip()

        # Validaciones
        if creador not in [usuario.nombre for usuario in Usuario.usuarios.values()]:
            print("Error: Usuario no encontrado. Registre un usuario primero.")
            return

        if not contenido:
            print("Error: El comentario no puede estar vacío.")
            return

        comentario = Comentario(pin_id, creador, contenido)
        cls.comentarios[comentario.id] = comentario
        print(f"Comentario agregado exitosamente al pin ID {pin_id}.")

def menu():
    while True:
        print("\n=== Menú Pinterest ===")
        print("1. Crear nuevo usuario")
        print("2. Crear nuevo tablero")
        print("3. Agregar nuevo pin a un tablero")
        print("4. Agregar comentario a un pin")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Usuario.crear_usuario()
        elif opcion == "2":
            Tablero.crear_tablero()
        elif opcion == "3":
            Pin.agregar_pin()
        elif opcion == "4":
            Comentario.agregar_comentario()
        elif opcion == "5":
            print("Saliendo de Pinterest...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
