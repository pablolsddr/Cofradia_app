from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask import render_template
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cofradia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Miembro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido1 = db.Column(db.String(50), nullable=False)
    apellido2 = db.Column(db.String(50), nullable=False)
    rut = db.Column(db.String(20), nullable=False, unique=True)
    digito_verificador = db.Column(db.String(2), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    correo = db.Column(db.String(100), nullable=True)
    edad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(200), nullable=True)



@app.route("/")
def home():
    miembros = Miembro.query.all()
    return render_template("index.html", miembros=miembros)

@app.route("/nuevo_miembro", methods=["GET", "POST"])
def nuevo_miembro():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido1 = request.form.get("apellido1")
        apellido2 = request.form.get("apellido2")
        edad = request.form.get("edad")
        fecha_nacimiento = request.form.get("fecha_nacimiento")

        nuevo_miembro_cofradia =Miembro(nombre=nombre, apellido=apellido1+" "+apellido2, edad=edad, fecha_nacimiento=fecha_nacimiento)
        db.session.add(nuevo_miembro_cofradia)
        db.session.commit()
        return redirect(url_for("/"))

    return render_template("/Nuevos_miembros.html")


#with asigna y lebera recursos
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

