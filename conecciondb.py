import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mi_base_datos"
    )
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos.")
except mysql.connector.Error as e:
    print("Error al conectar a la base de datos:", e)
