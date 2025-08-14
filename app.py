from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask import render_template
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cofradia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Miembro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)


@app.route("/")
def home():
    return render_template("index.html")

   





#with asigna y lebera recursos
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

