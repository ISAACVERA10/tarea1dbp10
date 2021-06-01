from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/ejercicio2db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3307/ejercicio2db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Profesor(db.Model):
    __tablename__ = 'profesor'
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return f'<Profesor: {self.id},{self.name}>'


class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return f'<Estudiante: {self.id},{self.name}>'

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(30), nullable=False)
    creditos = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Curso: {self.id},{self.name},{self.creditos}>'

class Seccion(db.Model):
    __tablename__ = 'seccion'
    id = db.Column(db.Integer, primary_key =True)
    codigo = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f'<Seccion: {self.id},{self.codigo}>'

db.create_all()
@app.route('/')
def index():
    return render_template('index.html',data1 = Profesor.query.all(),data2= Estudiante.query.all(),data3= Curso.query.all(),data4= Seccion.query.all())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
else:
    print('using global variables from FLASK')