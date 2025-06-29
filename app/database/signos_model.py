from datetime import datetime
from app.database import db
import uuid

class Signos(db.Model):
    __tablename__ = "signos"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(15), unique=True)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    caracteristicas = db.Column(db.String(400))
    # Relaciones
    predicciones = db.relationship('Predicciones', backref='signo_rel', lazy=True)
    imagenes = db.relationship('Imagenes', backref='signo_rel', lazy=True)

class Predicciones(db.Model):
    __tablename__ = "predicciones"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    fecha = db.Column(db.Date, default=datetime.utcnow)
    signo_id = db.Column(db.String(36), db.ForeignKey('signos.id'))
    prediccion = db.Column(db.String(500))
    
class Imagenes(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    signo = db.Column(db.Date)
    ubicacion = db.Column(db.String(15), nullable=True)