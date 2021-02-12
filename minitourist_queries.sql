CREATE TABLE IF NOT EXISTS usuarios
(
    id 			 INT AUTO_INCREMENT,
    nombre 		 VARCHAR(200) NOT NULL,
    direccion 	 VARCHAR(200) NOT NULL,
    ciudad 	 	 VARCHAR(100) NOT NULL,
    telefono 	 VARCHAR(10)  NOT NULL,
    email		 VARCHAR(100) NOT NULL,
    pass		 VARCHAR(20) NOT NULL,
    imagen		 VARCHAR(50)  NOT NULL,
    tipo_usuario VARCHAR(30)  NOT NULL,
    tipo_tarjeta VARCHAR(100)  NOT NULL,
    PRIMARY KEY (id)
);

SELECT *
FROM usuarios;

TRUNCATE TABLE usuarios;

INSERT INTO usuarios (nombre, direccion, ciudad, telefono, email, pass, imagen, tipo_usuario, tipo_tarjeta)
VALUES ('Luis Orlando Avila Garcia', 'Calle Ahuatla, colonia Las Cruces, Magdalena Contreras, CDMX', 'Ciudad de México', '5564191682', 'orlando.avilag@hotmail.com', 'LandoWolf10*',
'No aplica', 'Administrador', 'No aplica');

UPDATE usuarios SET nombre = 'Luis Orlando Avila Garcia', direccion = 'Calle Ahuatla, colonia Las Cruces, Magdalena Contreras, CDMX', ciudad = 'Ciudad de México',
imagen = 'No aplica', tipo_usuario = 'Administrador' WHERE id = 1;

DROP TABLE tarjetas;

CREATE TABLE IF NOT EXISTS tarjetas_status
(
    id 		INT AUTO_INCREMENT,
    nombre 	VARCHAR(200) NOT NULL,
    ciudad  VARCHAR(100) NOT NULL,
    tipo	VARCHAR(50)  NOT NULL,
    fecha 	DATE NOT NULL,
    PRIMARY KEY (id)
);

SELECT *
FROM tarjetas_status;

DELIMITER //
CREATE PROCEDURE spInsertUser
( 
    IN _nombre 			VARCHAR(200),
    IN _direccion 		VARCHAR(200),
    IN _ciudad 			VARCHAR(100),
    IN _tel 			VARCHAR(10), 
    IN _email 			VARCHAR(100),
    IN _pass 			VARCHAR(20),
    IN _imagen 			VARCHAR(50),
    IN _tipo_usuario 	VARCHAR(30),
    IN _tipo_tarjeta 	VARCHAR(100)
)
BEGIN
	INSERT INTO usuarios (nombre, direccion, ciudad, telefono, email, pass, imagen, tipo_usuario, tipo_tarjeta)  VALUES
	(_nombre, _direccion, _ciudad, _tel, _email, _pass, _imagen, _tipo_usuario, _tipo_tarjeta);
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spShowClients
( )
BEGIN
	SELECT *
    FROM usuarios AS u
    WHERE u.tipo_usuario = 'Cliente';
END//
DELIMITER ;

CALL spShowClients();
DELETE FROM usuarios WHERE id = 10;

DELIMITER //
CREATE PROCEDURE spDeleteClient
(
	IN clientID INT
)
BEGIN
	DELETE FROM usuarios WHERE id = clientID;
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spSelectClientImage
(
	IN clientID INT
)
BEGIN
	SELECT u.imagen
    FROM usuarios AS u
    WHERE u.id = clientID;
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spGetClientData
(
	IN clientID INT
)
BEGIN
	SELECT *
    FROM usuarios AS u
    WHERE u.id = clientID;
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spUpdateClient
(
    IN id_cliente			INT,
    IN nombre_cliente 	 	VARCHAR(200),
    IN direccion_cliente 	VARCHAR(200),
    IN telefono_cliente 	 VARCHAR(10),
    IN email_cliente 	 	VARCHAR(100),
    IN tarjeta 				VARCHAR(50)
)
BEGIN
	IF nombre_cliente IS NOT NULL THEN
    	UPDATE usuarios
        SET nombre = nombre_cliente
        WHERE id = id_cliente;
    END IF;
    
	IF direccion_cliente IS NOT NULL THEN
    	UPDATE usuarios 
        SET direccion = direccion_cliente
        WHERE id = id_cliente;
    END IF;
    
	IF telefono_cliente IS NOT NULL THEN
    	UPDATE usuarios 
        SET telefono = telefono_cliente
        WHERE id = id_cliente;
    END IF;
    
	IF email_cliente IS NOT NULL THEN
    	UPDATE usuarios 
        SET email = email_cliente
        WHERE id = id_cliente;
    END IF;
    
	IF tarjeta IS NOT NULL THEN
    	UPDATE usuarios 
        SET imagen = tarjeta
        WHERE id = id_cliente;
    END IF;
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spSelectClientLocation
(
	IN clientID INT
)
BEGIN
	SELECT u.ciudad, u.tipo_tarjeta
    FROM usuarios AS u
    WHERE u.id = clientID;
END//
DELIMITER ;

DROP PROCEDURE spSelectClientLocation;

SELECT *
FROM usuarios;

DELIMITER //
CREATE PROCEDURE spLogin
( 
    IN _email	VARCHAR(100),
    IN _pass 	VARCHAR(20)
)
BEGIN
	SELECT * 
    FROM usuarios
    WHERE email = _email AND pass = _pass;
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spTarjetaStatus
( 
    IN _nombre	VARCHAR(200),
    IN _ciudad	VARCHAR(100),
    IN _tipo	VARCHAR(50)
)
BEGIN
	INSERT INTO tarjetas_status(nombre, ciudad, tipo, fecha) 
    VALUES (_nombre, _ciudad, _tipo, CURDATE());
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spMostrarVisitas
( 
    IN nombre_tarjeta VARCHAR (100)
)
BEGIN
	SELECT COUNT(ts.nombre) AS cantidad_visitas
	FROM tarjetas_status AS ts
	WHERE ts.nombre = nombre_tarjeta AND ts.tipo = 'Visita';
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spMostrarDescargas
( 
    IN nombre_tarjeta VARCHAR (100)
)
BEGIN
	SELECT COUNT(ts.nombre) AS cantidad_descargas
	FROM tarjetas_status AS ts
	WHERE ts.nombre = nombre_tarjeta AND ts.tipo = 'Descarga';
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spMostrarDescargasFecha
(
	IN nombre_tarjeta VARCHAR (100),
    IN _fecha DATE
)
BEGIN
	SELECT COUNT(ts.nombre) AS cantidad_descargas
	FROM tarjetas_status AS ts
	WHERE ts.nombre = nombre_tarjeta AND ts.fecha = _fecha AND ts.tipo = 'Descarga';
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spMostrarVisitasFecha
(
	IN nombre_tarjeta VARCHAR (100),
    IN _fecha DATE
)
BEGIN
	SELECT COUNT(ts.nombre) AS cantidad_visitas
	FROM tarjetas_status AS ts
	WHERE ts.nombre = nombre_tarjeta AND ts.fecha = _fecha AND ts.tipo = 'Visita';
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spMostrarDescargasRangoFecha
(
	IN nombre_tarjeta VARCHAR (100),
    IN fecha_inicio DATE,
    IN fecha_fin DATE
)
BEGIN
	SELECT COUNT(ts.nombre) AS cantidad_descargas
	FROM tarjetas_status AS ts
	WHERE ts.nombre = nombre_tarjeta AND ts.fecha BETWEEN fecha_inicio AND fecha_fin AND ts.tipo = 'Descarga';
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spMostrarVisitasRangoFecha
(
	IN nombre_tarjeta VARCHAR (100),
    IN fecha_inicio DATE,
    IN fecha_fin DATE
)
BEGIN
	SELECT COUNT(ts.nombre) AS cantidad_visitas
	FROM tarjetas_status AS ts
	WHERE ts.nombre = nombre_tarjeta AND ts.fecha BETWEEN fecha_inicio AND fecha_fin AND ts.tipo = 'Visita';
END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE spContarTarjetasLugaresZihua
()
BEGIN
	SELECT COUNT(u.nombre) AS cantidad
	FROM usuarios AS u
	WHERE u.Ciudad = 'Zihuatanejo' AND u.tipo_tarjeta = 'lugares';
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE spContarTarjetasRestZihua
()
BEGIN
	SELECT COUNT(u.nombre) AS cantidad
	FROM usuarios AS u
	WHERE u.Ciudad = 'Zihuatanejo' AND u.tipo_tarjeta = 'restaurantes';
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE spContarTarjetasParquesZihua
()
BEGIN
	SELECT COUNT(u.nombre) AS cantidad
	FROM usuarios AS u
	WHERE u.Ciudad = 'Zihuatanejo' AND u.tipo_tarjeta = 'parques';
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE spContarTarjetasTiendasZihua
()
BEGIN
	SELECT COUNT(u.nombre) AS cantidad
	FROM usuarios AS u
	WHERE u.Ciudad = 'Zihuatanejo' AND u.tipo_tarjeta = 'tiendas';
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE spContarTarjetasServiciosZihua
()
BEGIN
	SELECT COUNT(u.nombre) AS cantidad
	FROM usuarios AS u
	WHERE u.Ciudad = 'Zihuatanejo' AND u.tipo_tarjeta = 'servicios';
END//
DELIMITER ;

DROP PROCEDURE spContarTarjetasZihua;

SELECT *
FROM usuarios;

SELECT *
FROM tarjetas_status;

CALL spMostrarDescargasFecha('Believe.jpg', '2020-11-17');
CALL spMostrarVisitasFecha('Believe.jpg', '2020-11-17');
CALL spMostrarDescargasRangoFecha('Believe.jpg', '2020-11-10', '2020-11-17');



CALL spMostrarVisitas('Believe.jpg');

DROP PROCEDURE spMostrarTarjetaStatus;
DROP PROCEDURE spMostrarDescargas;


DROP PROCEDURE spTarjetaStatus;


CALL spTarjetaVisita('Prueba');


INSERT INTO tarjetas_status (nombre, ciudad, tipo, fecha)
VALUES ('Believe.jpg', 'Acapulco', 'Descarga', '2020-11-05');


SELECT COUNT(vt.nombre) AS cantidad_visitas
FROM tarjetas_status AS vt
WHERE vt.nombre = 'Believe.jpg' AND vt.tipo = 'Descarga';

SELECT COUNT(vt.nombre) AS cantidad_visitas
FROM tarjetas_status AS vt
WHERE vt.nombre = 'Believe.jpg' AND vt.fecha = '2020-11-05';

SELECT *
FROM tarjetas_status;

TRUNCATE TABLE tarjetas_status;

SELECT *
FROM usuarios;

DELETE FROM usuarios WHERE id = 4;

TRUNCATE TABLE usuarios;