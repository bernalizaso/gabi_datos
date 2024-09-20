CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL
);

DELIMITER //

CREATE PROCEDURE crear_usuario(IN nombre VARCHAR(100), IN correo VARCHAR(100))
BEGIN
    INSERT INTO usuarios (nombre, correo) VALUES (nombre, correo);
END //

CREATE PROCEDURE leer_usuarios()
BEGIN
    SELECT * FROM usuarios;
END //

CREATE PROCEDURE actualizar_usuario(IN usuario_id INT, IN nuevo_nombre VARCHAR(100), IN nuevo_correo VARCHAR(100))
BEGIN
    UPDATE usuarios SET nombre = nuevo_nombre, correo = nuevo_correo WHERE id = usuario_id;
END //

CREATE PROCEDURE eliminar_usuario(IN usuario_id INT)
BEGIN
    DELETE FROM usuarios WHERE id = usuario_id;
END //

DELIMITER ;
