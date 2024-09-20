from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar base de datos y ORM
Base = declarative_base()
engine = create_engine('sqlite:///usuarios.db')
Session = sessionmaker(bind=engine)
session = Session()

# Definir la clase Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    correo = Column(String)

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)


def crear_usuario(nombre, correo):
    nuevo_usuario = Usuario(nombre, correo)
    session.add(nuevo_usuario)
    session.commit()
    print(f"Usuario {nombre} creado con exito.")


def leer_usuarios():
    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Correo: {usuario.correo}")


def actualizar_usuario(usuario_id, nuevo_nombre, nuevo_correo):
    usuario = session.query(Usuario).filter_by(id=usuario_id).first()
    if usuario:
        usuario.nombre = nuevo_nombre
        usuario.correo = nuevo_correo
        session.commit()
        print(f"Usuario {usuario_id} actualizado con exito.")
    else:
        print("Usuario no encontrado.")


def eliminar_usuario(usuario_id):
    usuario = session.query(Usuario).filter_by(id=usuario_id).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f"Usuario {usuario_id} eliminado con exito.")
    else:
        print("Usuario no encontrado.")



crear_usuario("Juan Perez", "juan@example.com")


leer_usuarios()


actualizar_usuario(1, "Juan Actualizado", "juan.actualizado@example.com")


leer_usuarios()


eliminar_usuario(1)
