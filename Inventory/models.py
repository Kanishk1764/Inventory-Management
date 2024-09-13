from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CarDue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_no = db.Column(db.String(50), nullable=False)
    model_name = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    dealership = db.Column(db.String(100), nullable=False)
    parts = db.relationship('Part', backref='car_due', lazy=True)

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    car_due_id = db.Column(db.Integer, db.ForeignKey('car_due.id'), nullable=False)
