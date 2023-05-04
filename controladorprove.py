from config import conectar

def insertar_prov(id_proveedores,nombre_proveedor,numero_telefonico):
    conexion= conectar()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO telefonos(id_proveedores,nombre_proveedor,numero_telefonico) VALUES (%s, %s, %s,%s, %s, %s)",
                       (id_proveedores,nombre_proveedor,numero_telefonico))
    conexion.commit()
    conexion.close()

def obtener_prov():
    conexion= conectar()
    proveedores = []
    with conexion.cursor() as cursor:
        cursor.execute("Select id_proveedores,nombre_proveedor,numero_telefonico")
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
        cursor.execute("UPDATE proveedores SET nombre_proveedor = %s,numero_telefonico = %s, WHERE id_proveedores = %s",
                       (id_proveedores,nombre_proveedor,numero_telefonico))
    conexion.commit()
    conexion.close()