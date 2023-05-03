from flask import Flask, render_template, request
from config import conectar
from flask_mysqldb import MySQL

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

    
if __name__ == '__main__':
    app.run(debug=True)