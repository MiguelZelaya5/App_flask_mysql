from config import conectar

def insertar_prov(id_proveedores,nombre_proveedor,numero_telefonico,estado):
    conexion= conectar()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO telefonos(id_proveedores,nombre_proveedor,numero_telefonico,estado) VALUES (%s, %s, %s,%s, %s, %s, %s)",
                       (id_proveedores,nombre_proveedor,numero_telefonico,estado))
    conexion.commit()
    conexion.close()

def obtener_prov():
    conexion= conectar()
    proveedores = []
    with conexion.cursor() as cursor:
        cursor.execute("Select id_proveedores,nombre_proveedor,numero_telefonico,estado FROM proveedores")
        proveedores = cursor.fetchall()
    conexion.close()
    return proveedores

def eliminar_prov(id_proveedores):
    conexion= conectar()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE proveedores SET estado = 'I' where id_proveedores=%s",
                       (id_proveedores))
    conexion.commit()
    conexion.close()

def actualizar_prov(id_proveedores,nombre_proveedor,numero_telefonico):
    conexion = conectar()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE proveedores SET nombre_proveedor = %s,numero_telefonico = %s,estado = %s WHERE id_proveedores = %s",
                       (id_proveedores,nombre_proveedor,numero_telefonico))
    conexion.commit()
    conexion.close()

def obtener_prove_por_id(id_proveedores):
    conexion = conectar()
    cursor=conexion.cursor()
    cursor.execute("SELECT id_proveedores, nombre_proveedor, numero_telefonico,estado  WHERE id_proveedores = %s",(id_proveedores))
    actu= cursor.fetchone()
    return actu