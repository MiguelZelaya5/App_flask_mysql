from flask import Flask, render_template, request,redirect
import result
from flask_mysqldb import MySQL
from wtforms import SelectField
from flask_wtf import FlaskForm
import controladortele
import controladorprove
import controladorclien
import controladorcompra
from mysql.connector import connect
from config import conectar
import mysql.connector

app = Flask(__name__)
mydb = conectar
mysql = MySQL(app)

usuarios = [
    {"usuario": "juan", "contraseña": "1234"},
    {"usuario": "ana", "contraseña": "abcd"},
    {"usuario": "pedro", "contraseña": "qwerty"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cerrarCesion")
def cerrarCesion():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form["usuario"]
    contraseña = request.form["contraseña"]
    
    for u in usuarios:
        if u["usuario"] == usuario and u["contraseña"] == contraseña:
            return redirect("menuPricipal")
    
    return "Usuario o contraseña incorrectos"

@app.route("/formularioagregartelefono")
def formularioagregartelefono():
     return render_template("agregartelefono.html")
@app.route("/formularioagregarproveedor")
def formularioagregarproveedor():
     return render_template("agregarprov.html")
@app.route("/insert", methods=["POST"])
def insert():
    nombre_telefono = request.form["nombre_telefono"]
    marca = request.form["marca"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    existencias=request.form["existencias"]
    proveedor=request.form["proveedor"]
    estado= request.form["estado"]
    controladortele.insertar_telefono(nombre_telefono,marca,descripcion,
                                      precio,existencias,proveedor,estado)
    return redirect("/tablatel")

@app.route("/tablatelefonos")
def tablatelefonos():
    tablatelefonos = controladortele.obtener_telefonos()
    return render_template("tablatelefonos.html",tablatelefonos=tablatelefonos)

@app.route('/proveedores')
def proveedores():
    proveedores=controladortele.obtener_name_proveedores()
   
    return render_template("agregartelefono.html", proveedores=proveedores)

@app.route("/tablatel")
def tablatel():
    proveedores=controladortele.obtener_name_proveedores()
    tablatelefonos = controladortele.obtener_telefonos()
    return render_template("agregartelefono.html",tablatelefonos=tablatelefonos,proveedores=proveedores)

@app.route("/eliminar_telefono", methods=["POST"])
def eliminar_telefono():
    id = request.form["id"]
    controladortele.eliminar_telefono(id)
    return redirect("/tablatelefonos")

@app.route("/formulario_editar_telefono/<int:id_telefono>")
def formulario_editar_telefono(id_telefono):
    # Obtener el juego por ID
    proveedores=controladortele.obtener_name_proveedores()
    editar_telefono= controladortele.obtener_telefono_por_id(id_telefono)
    return render_template("edittele.html", editar_telefono=editar_telefono,proveedores=proveedores)


@app.route("/actualizar_telefono", methods=["POST"])
def actualizar_telefono():
    id_telefono = request.form["id_telefono"]
    nombre_telefono = request.form["nombre_telefono"]
    marca = request.form["marca"]

    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    existencias = request.form["existencias"]
    id_proveedor = request.form["proveedor"]
    estado=request.form["estado"]
    controladortele.actualizar_telefonos(nombre_telefono,marca,descripcion,precio,
                        existencias,id_proveedor,estado,id_telefono)
    return redirect("/tablatelefonos")



@app.route("/mostrartodoslosproveedores")
def mostrartodoslosproveedores():
    mostrartodoslosproveedores=controladorprove.obtener_prov()
    return render_template("tablaproveedor.html",mostrartodoslosproveedores=mostrartodoslosproveedores)

@app.route("/mostrartodoslosproveedoresinsert")
def mostrartodoslosproveedoresinsert():
    mostrartodoslosproveedores=controladorprove.obtener_prov()
    return render_template("agregarprov.html",mostrartodoslosproveedores=mostrartodoslosproveedores)

@app.route("/insertarproveedor", methods=["POST"])
def insertarproveedor():
    nombre_proveedor = request.form["nombre_proveedor"]
    numero_telefonico=request.form["numero_telefonico"]
    estado=request.form["estado"]
    controladorprove.insertar_prov(nombre_proveedor,numero_telefonico,estado)
    return redirect("/mostrartodoslosproveedoresinsert")

@app.route("/eliminar_proveedor", methods=["POST"])
def eliminar_proveedor():
    id = request.form["id"]
    controladorprove.eliminar_prov(id)
    return redirect("/mostrartodoslosproveedores")

@app.route("/actualizar_proveedor", methods=["POST"])
def actualizar_proveedor():
    id_proveedores = request.form["id_proveedores"]
    nombre_proveedor = request.form["nombre_proveedor"]
    numero_telefonico = request.form["numero_telefonico"]
    estado=request.form["estado"]
    
    controladorprove.actualizar_prov(id_proveedores,nombre_proveedor,numero_telefonico,estado)
    return redirect("/mostrartodoslosproveedores")

@app.route("/formulario_editar_proveedor/<int:id_proveedores>")
def formulario_editar_proveedor(id_proveedores):
    # Obtener el juego por ID
    obtenpro_id=controladorprove.obtener_prove_por_id(id_proveedores)
    return render_template("editprove.html", obtenpro_id=obtenpro_id)

#----------------------metodos de cliente-------------------------------
@app.route("/mostrartodoslosclientes")
def mostrartodoslosclientes():
    mostrartodoslosclientes=controladorclien.obtener_clientes()
    return render_template("tablaclientes.html",mostrartodoslosclientes=mostrartodoslosclientes)

@app.route("/mostrartodoslosclientesinsert")
def mostrartodoslosclientesinsert():
    mostrartodoslosclientesinsert=controladorclien.obtener_clientes()
    return render_template("agregarclien.html",mostrartodoslosclientesinsert=mostrartodoslosclientesinsert)

@app.route("/insertarcliente", methods=["POST"])
def insertarcliente():
    nombre_cliente = request.form["nombre_cliente"]
    numero_telefono=request.form["numero_telefono"]
    direccion=request.form["direccion"]
    controladorclien.insertar_clientes(nombre_cliente,numero_telefono,direccion)
    return redirect("/mostrartodoslosclientesinsert")

@app.route("/eliminar_cliente", methods=["POST"])
def eliminar_cliente():
    id = request.form["id"]
    controladorclien.eliminar_cliente(id)
    return redirect("/mostrartodoslosclientes")

@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    id_clientes = request.form["id_clientes"]
    nombre_cliente = request.form["nombre_cliente"]
    numero_telefono = request.form["numero_telefono"]
    direccion=request.form["direccion"]
    
    controladorclien.actualizar_clientes(nombre_cliente,numero_telefono,direccion,id_clientes)
    return redirect("/mostrartodoslosclientes")

@app.route("/formulario_editar_cliente/<int:id_clientes>")
def formulario_editar_cliente(id_clientes):
    # Obtener el juego por ID
    obtenclien_id=controladorclien.obtener_cliente_por_id(id_clientes)
    return render_template("editclientes.html", obtenclien_id=obtenclien_id)

#----------------------metodos de cliente-------------------------------
@app.route("/mostrarteleymostrarcompra")
def mostrarteleymostrarcompra():
    nombrestele=controladorcompra.obtener_name_telefono()
    nombrecliente=controladorcompra.obtener_name_cliente()
    tablacompra=controladorcompra.obtener_compra()
    return render_template("agregarcompra.html",nombrestele=nombrestele,nombrecliente=nombrecliente,tablacompra=tablacompra)

@app.route("/mostrartodoslascompras")
def mostrartodoslascompras():
    mostrartodoslascompras=controladorcompra.obtener_compra()
    return render_template("tablacompra.html",mostrartodoslascompras=mostrartodoslascompras)

@app.route("/insertarcompra", methods=["POST"])
def insertarcompra():
    id_cliente=request.form["id_cliente"]
    id_telefono=request.form["id_telefono"]
    cantidad=request.form["cantidad"]
    precio=request.form["precio"]
    fecha_compra=request.form["fecha_compra"]
    estado=request.form["estado"]
    controladorcompra.insertar_compra(id_cliente,id_telefono,cantidad,precio,fecha_compra,estado)
    return redirect("/mostrarteleymostrarcompra")

@app.route("/eliminar_compra", methods=["POST"])
def eliminar_compra():
    id = request.form["id"]
    controladorcompra.eliminar_compra(id)
    return redirect("/mostrartodoslascompras")

@app.route("/actualizar_compra", methods=["POST"])
def actualizar_compra():
    id_compra=request.form["id_compra"]
    id_cliente = request.form["id_cliente"]
    id_telefono = request.form["id_telefono"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]
    fecha_compra=request.form["fecha_compra"]
    estado=request.form["estado"]
    controladorcompra.actualizar_compra(id_cliente,id_telefono,cantidad,precio,fecha_compra,estado,id_compra)
    return redirect("/mostrartodoslascompras")

@app.route("/formulario_editar_compra/<int:id_compra>")
def formulario_editar_compra(id_compra):
    # Obtener el juego por ID
    obtencompra_id=controladorcompra.obtener_compra_por_id(id_compra)
    obtencompraall=controladorcompra.obtener_name_cliente()
    obtenteleall=controladorcompra.obtener_name_telefono()
    return render_template("editcompra.html", obtencompra_id=obtencompra_id, obtencompraall=obtencompraall, obtenteleall=obtenteleall)

@app.route("/menuPricipal")
def menuPricipal():
    tablatelefonos = controladortele.obtener_telefonos()
    mostrartodoslosproveedores=controladorprove.obtener_prov()
    mostrartodoslosclientes=controladorclien.obtener_clientes()
    mostrartodoslascompras=controladorcompra.obtener_compra()
    
    return render_template("menuprincipal.html",tablatelefonos=tablatelefonos, mostrartodoslosproveedores=mostrartodoslosproveedores, mostrartodoslosclientes=mostrartodoslosclientes, mostrartodoslascompras=mostrartodoslascompras)

if __name__ == '__main__':
    app.run(port=3000,debug=True)