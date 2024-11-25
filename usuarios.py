class Usuario:
    def __init__(self, conexion):
        self.conexion = conexion

    def iniciar_sesion(self):
        """
        Permite a un usuario iniciar sesión.
        """
        correo = input("Correo: ")
        contrasena = input("Contraseña: ")

        cursor = self.conexion.cursor(dictionary=True)
        query = "SELECT id_usuario, nombre_completo FROM usuarios WHERE correo = %s AND contrasena = %s"
        cursor.execute(query, (correo, contrasena))
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            print(f"Bienvenido, {resultado['nombre_completo']}!")
            return resultado["id_usuario"]
        return None

    def crear_usuario(self):
        """
        Permite crear un nuevo usuario.
        """
        print("\n--- Crear Usuario ---")
        nombre = input("Nombre completo: ")
        correo = input("Correo: ")
        contrasena = input("Contraseña: ")

        cursor = self.conexion.cursor()
        query = "INSERT INTO usuarios (nombre_completo, correo, contrasena) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (nombre, correo, contrasena))
            self.conexion.commit()
            print("Usuario creado exitosamente.")
        except mysql.connector.Error as e:
            print(f"Error al crear el usuario: {e}")
        finally:
            cursor.close()
