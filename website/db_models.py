from . import db
from sqlalchemy.sql import func

class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    init_odo = db.Column(db.Integer)
    current_odo = db.Column(db.Integer, nullable=True)
    odo_unit = db.Column(db.String(2))
    
    refuelings = db.relationship('Refuel')
    
    def __repr__(self):
        return f"{self.brand} {self.model}"
    
class Refuel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    refuel_odo = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)