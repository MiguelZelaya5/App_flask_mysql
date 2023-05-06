from flask import Flask, render_template, request,redirect
import result
from flask_mysqldb import MySQL
from wtforms import SelectField
from flask_wtf import FlaskForm
import controladortele
import controladorprove
from mysql.connector import connect
from config import conectar
import mysql.connector

app = Flask(__name__)
mydb = conectar
mysql = MySQL(app)


@app.route("/formularioagregartelefono")
def formularioagregartelefono():
     return render_template("agregartelefono.html")
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
@app.route("/")
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
    return render_template("tablaproveedores.html",mostrartodoslosproveedores=mostrartodoslosproveedores)

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
    return redirect("/agregarprov.html")

@app.route("/eliminar_proveedor", methods=["POST"])
def eliminar_proveedor():
    id = request.form["id"]
    controladorprove.eliminar_prov(id)
    return redirect("/tablaproveedor")

@app.route("/actualizar_proveedor", methods=["POST"])
def actualizar_proveedor():
    id_proveedores = request.form["id_proveedores"]
    nombre_proveedor = request.form["nombre_proveedor"]
    numero_telefonico = request.form["numero_telefonico"]
    estado=request.form["estado"]
    
    controladortele.actualizar_telefonos(id_proveedores,nombre_proveedor,numero_telefonico,estado)
    return redirect("/tablatelefonos")

@app.route("/formulario_editar_proveedor/<int:id_proveedores>")
def formulario_editar_telefono(id_proveedores):
    # Obtener el juego por ID
    obtenpro_id=controladorprove.obtener_prove_por_id(id_proveedores)
    return render_template("editprove.html", obtenpro_id=obtenpro_id)







if __name__ == '__main__':
    app.run(port=3000,debug=True)