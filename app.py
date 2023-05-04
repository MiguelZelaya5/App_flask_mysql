from flask import Flask, render_template, request,redirect
from config import conectar
from flask_mysqldb import MySQL
import controladortele

app = Flask(__name__)
mydb = conectar()
mysql = MySQL(mydb)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    email=request.form('email')
    password = request.form('password')

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
    return redirect("/tablatelefonos")
@app.route("/")
@app.route("/tablatelefonos")
def mostrartele():
    telefonostable = controladortele.obtener_telefonos
    return render_template("tablatelefonos.html", telefonostable=telefonostable)

@app.route("/eliminar_telefono", methods=["POST"])
def eliminar_telefono():
    id = request.form["id"]
    controladortele.eliminar_telefono(id)
    return redirect("/tablatelefonos")

@app.route("/actualizar_juego", methods=["POST"])
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
    app.run(debug=True)