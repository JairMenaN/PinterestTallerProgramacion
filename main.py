import mysql.connector
from usuarios import Usuario
#from tablero import Tablero
#from pin import Pin
#from comentario import Comentario

#ACTUALIANDO CONEXION
class AplicacionPinterest:
    def __init__(self):
        self.conexion = self.crear_conexion()
        self.usuario_actual = None

    def crear_conexion(self):
        """
        Establece una conexión con la base de datos MySQL.
        """
        try:
            conexion = mysql.connector.connect(
                host="localhost",  # Cambiar si el servidor no es local
                user="root",  # Usuario de MySQL
                password="",  # Contraseña de MySQL 
                database="pinterest"  # Nombre de la base de datos
            )
            if conexion.is_connected():
                print("Conexión exitosa a la base de datos.")
            return conexion
        except mysql.connector.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    def menu_principal(self):
        """
        Muestra el menú principal de la aplicación.
        """
        while True:
            print("\nMenú Principal")
            print("1. Iniciar sesión")
            print("2. Crear cuenta")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.iniciar_sesion()
            elif opcion == "2":
                self.crear_cuenta()
            elif opcion == "3":
                print("Gracias por usar Pinterest CLI.")
                self.conexion.close()
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def iniciar_sesion(self):
        """
        Permite a un usuario iniciar sesión.
        """
        usuario = Usuario(self.conexion)
        self.usuario_actual = usuario.iniciar_sesion()
        if self.usuario_actual:
            print("Inicio de sesión exitoso.")
            self.menu_usuario()
        else:
            print("Credenciales inválidas.")

    def crear_cuenta(self):
        """
        Permite crear un nuevo usuario.
        """
        usuario = Usuario(self.conexion)
        usuario.crear_usuario()

    def menu_usuario(self):
        """
        Muestra el menú para usuarios logueados.
        """
        while True:
            print("\nMenú del Usuario")
            print("1. Gestión de Tableros")
            print("2. Gestión de Pines")
            print("3. Gestión de Comentarios")
            print("4. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                tablero = Tablero(self.conexion, self.usuario_actual)
                tablero.menu_tableros()
            elif opcion == "2":
                pin = Pin(self.conexion, self.usuario_actual)
                pin.menu_pines()
            elif opcion == "3":
                comentario = Comentario(self.conexion, self.usuario_actual)
                comentario.menu_comentarios()
            elif opcion == "4":
                print("Cerrando sesión...")
                self.usuario_actual = None
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    app = AplicacionPinterest()
    app.menu_principal()
