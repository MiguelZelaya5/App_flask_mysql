from config import conectar

def insertar_telefono(nombre_telefono,marca,descripcion,precio,existencias,id_proveedor,estado):
    conexion= conectar()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO telefonos(nombre_telefono,marca,descripcion,precio,existencias,id_proveedor,estado) VALUES (%s, %s, %s,%s, %s, %s, %s)",
                       (nombre_telefono,marca,descripcion,precio,existencias,id_proveedor,estado))
    conexion.commit()
    conexion.close()

def obtener_telefonos():
    conexion= conectar()
    telefonos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT t.id_telefono, t.nombre_telefono, t.marca, t.descripcion, t.precio, t.existencias, p.nombre_proveedor,t.estado FROM telefonos t INNER JOIN proveedores p ON t.id_proveedor=p.id_proveedores ORDER BY id_telefono asc")
        telefonos = cursor.fetchall()
    conexion.close()
    return telefonos


def eliminar_telefono(id_telefono):
    conexion= conectar()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE telefonos SET estado = 'I' where id_telefono=%s",
                       (id_telefono))
    conexion.commit()
    conexion.close()

def actualizar_telefonos(nombre_telefono,marca,descripcion,precio,existencias,id_proveedor,id_telefono,estado):
    conexion = conectar()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE telefonos SET nombre_telefono = %s,marca = %s,descripcion = %s, precio = %s, existencias = %s, id_proveedor = %s, estado = %s WHERE id_telefono = %s",
                       (nombre_telefono, marca,descripcion, precio,existencias,id_proveedor,id_telefono,estado))
    conexion.commit()
    conexion.close()

def obtener_name_proveedores():
    conexion= conectar()
    cursor=conexion.cursor()
    cursor.execute("select id_proveedores, nombre_proveedor from proveedores where estado='A'")
    proveedores = cursor.fetchall()  
    return proveedores

def obtener_telefono_por_id(id_telefono):
    conexion = conectar()
    cursor=conexion.cursor()
    cursor.execute("SELECT t.id_telefono,t.nombre_telefono,t.marca,t.descripcion,t.precio,t.existencias,p.id_proveedores,p.nombre_proveedor,t.estado from telefonos t inner join proveedores p on t.id_proveedor=p.id_proveedores WHERE t.id_telefono = %s",(id_telefono))
    actu= cursor.fetchone()
    return actu