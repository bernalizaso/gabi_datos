import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host='localhost',  # Cambia esto si tu servidor es diferente
    user='tu_usuario',  # Cambia esto por tu usuario de MySQL
    password='tu_contraseña',  # Cambia esto por tu contraseña
    database='tu_base_de_datos'  # Cambia esto por tu base de datos
)

def crear_usuario(nombre, correo):
    with conexion.cursor() as cursor:
        cursor.callproc('crear_usuario', (nombre, correo))
        conexion.commit()
        print(f"Usuario {nombre} creado con éxito.")

def leer_usuarios():
    with conexion.cursor() as cursor:
        cursor.callproc('leer_usuarios')
        for resultado in cursor.stored_results():
            usuarios = resultado.fetchall()
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}")

def actualizar_usuario(usuario_id, nuevo_nombre, nuevo_correo):
    with conexion.cursor() as cursor:
        cursor.callproc('actualizar_usuario', (usuario_id, nuevo_nombre, nuevo_correo))
        conexion.commit()
        print(f"Usuario {usuario_id} actualizado con éxito.")

def eliminar_usuario(usuario_id):
    with conexion.cursor() as cursor:
        cursor.callproc('eliminar_usuario', (usuario_id,))
        conexion.commit()
        print(f"Usuario {usuario_id} eliminado con éxito.")

# Ejemplos de uso
crear_usuario("Juan Perez", "juan@example.com")
leer_usuarios()
actualizar_usuario(1, "Juan Actualizado", "juan.actualizado@example.com")
leer_usuarios()
eliminar_usuario(1)

# Cerrar la conexión
conexion.close()
