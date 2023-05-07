from config import conectar

def insertar_clientes(nombre_cliente,numero_telefono,direccion, estado):
    conexion= conectar()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO clientes(nombre_cliente,numero_telefono,direccion,estado) VALUES (%s, %s, %s,%s)",
                       (nombre_cliente,numero_telefono,direccion,estado))
    conexion.commit()
    conexion.close()

def obtener_clientes():
    conexion= conectar()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute("select id_clientes, nombre_cliente, numero_telefono, direccion, estado from clientes")
        clientes = cursor.fetchall()
    conexion.close()
    return clientes

def eliminar_cliente(id_clientes):
    conexion= conectar()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET estado = 'I' where id_clientes=%s",
                       (id_clientes))
    conexion.commit()
    conexion.close()

def actualizar_clientes(nombre_cliente,numero_telefono,direccion,estado,id_clientes):
    conexion = conectar()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET nombre_cliente = %s,numero_telefono = %s, direccion = %s, estado=%s WHERE id_clientes = %s",
                       (nombre_cliente,numero_telefono,direccion,estado,id_clientes))
    conexion.commit()
    conexion.close()

def obtener_cliente_por_id(id_cliente):
    conexion = conectar()
    cursor=conexion.cursor()
    cursor.execute("SELECT  id_clientes, nombre_cliente, numero_telefono, direccion, estado from clientes WHERE id_clientes = %s",(id_cliente))
    actu= cursor.fetchone()
    return actu