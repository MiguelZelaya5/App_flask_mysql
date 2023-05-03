import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="app",
    password="Hola1234",
    database="telefonosdb"
)

if mydb.is_connected():
    print('Conexión exitosa!')
else:
    print('Error de conexión.')
