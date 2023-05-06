from config import conectar

def insertar_compra(id_cliente,id_telefono,cantidad,precio,fecha_compra):
    conexion= conectar()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO compra(id_cliente,id_telefono,cantidad,precio,fecha_compra) VALUES (%s, %s, %s, %s, %s)",
                       (id_cliente,id_telefono,cantidad,precio,fecha_compra))
    conexion.commit()
    conexion.close()

def obtener_compra():
    conexion= conectar()
    compra = []
    with conexion.cursor() as cursor:
        cursor.execute("select c.id_compra, cl.nombre_cliente, t.nombre_telefono, c.cantidad, c.precio, c.fecha_compra from compra c INNER JOIN clientes cl ON c.id_cliente = cl.id_clientes INNER JOIN telefonos t on c.id_telefono=t.id_telefono ")
        compra = cursor.fetchall()
    conexion.close()
    return compra

def eliminar_compra(id_compra):
    conexion= conectar()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE compra SET estado = 'I' where id_compra=%s",
                       (id_compra))
    conexion.commit()
    conexion.close()

def actualizar_compra(id_compra,id_cliente,id_telefono,cantidad,precio,fecha_compra,estado):
    conexion = conectar()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE compra SET id_cliente= %s,id_telefono= %s, cantidad = %s, precio = %s, fecha_compra = %s, estado = %s  WHERE id_compra = %s",
                       (id_cliente, id_telefono,cantidad, precio, fecha_compra,estado, id_compra))
    conexion.commit()
    conexion.close()

def obtener_name_cliente():
    conexion= conectar()
    cursor=conexion.cursor()
    cursor.execute("select id_clientes, nombre_cliente from clientes")
    clientes = cursor.fetchall()  
    return clientes

def obtener_name_telefono():
    conexion= conectar()
    cursor=conexion.cursor()
    cursor.execute("SELECT id_telefono, nombre_telefono FROM telefonos")
    telefonos = cursor.fetchall()  
    return telefonos

def obtener_compra_por_id(id_compra):
    conexion = conectar()
    cursor=conexion.cursor()
    cursor.execute("select c.id_compra , c.id_cliente, cl.nombre_cliente, c.id_telefono, te.nombre_telefono, c.cantidad, c.precio , c.fecha_compra, c.estado  from compra c inner join clientes cl on c.id_cliente=cl.id_clientes inner join telefonos te on c.id_telefono=te.id_telefono WHERE c.id_compra = %s",(id_compra))
    actu= cursor.fetchone()
    return actu