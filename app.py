from flask import Flask, render_template, request,redirect
import result
from flask_mysqldb import MySQL
from wtforms import SelectField
from flask_wtf import FlaskForm
import controladortele
from mysql.connector import connect
from config import conectar
import mysql.connector

app = Flask(__name__)
mydb = conectar
mysql = MySQL(app)

@app.route("/agregartelefonos")
def formulariotelefono():
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
    return redirect("/tablatelefonos.html")
@app.route("/")
@app.route("/tablatelefonos")
def tablatelefonos():
    tablatelefonos = controladortele.obtener_telefonos()
    return render_template("tablatelefonos.html", tablatelefonos=tablatelefonos)

@app.route('/proveedores')
def proveedores():
    proveedores=controladortele.obtener_name_proveedores()
   
    return render_template("agregartelefono.html", proveedores=proveedores)

@app.route("/eliminar_telefono", methods=["POST"])
def eliminar_telefono():
    id = request.form["id"]
    controladortele.eliminar_telefono(id)
    return redirect("/tablatelefonos")

@app.route("/actualizar_telefono", methods=["POST"])
def actualizar_juego():
    id_telefono = request.form["id_telefono"]
    nombre_telefono = request.form["nombre_telefono"]
    marca = request.form["descripcion"]

    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    existencias = request.form["existencias"]
    id_proveedor = request.form["id_proveedor"]
    controladortele.actualizar_telefonos(nombre_telefono,marca,descripcion,precio,
                        existencias,id_proveedor,id_telefono)
    return redirect("/tablatelefonos")



if __name__ == '__main__':
    app.run(port=3000,debug=True)