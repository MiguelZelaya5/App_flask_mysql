import pymysql


def conectar():
    return pymysql.connect(host='localhost',
                                user='app',
                                password='Hola1234',
                                db='telefonosdb')