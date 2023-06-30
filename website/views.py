from flask import Blueprint, render_template
from .db_models import Car, Refuel
from . import db
from flask import request

views = Blueprint("views", __name__)

@views.route("/", methods = ['POST', 'GET'])
def index():
    # new_car= Car(brand='Opel', model='Corsa', init_odo=12345, current_odo='', odo_unit='km')
    # db.session.add(new_car)
    # db.session.commit()
    cars = Car.query.all()
    if request.method == "POST":
        id = request.form["car_id"]
        Car.query.filter_by(id=id).delete()
        db.session.commit()
    return render_template("show_cars.html", cars = cars)

@views.route("/add_car", methods = ['POST', 'GET'])
def add():
    if request.method == "POST":
        
        brand_ = request.form['brand']
        model_ = request.form['model']
        odo_ = request.form['odo']
        unit_ = request.form['unit']
        
        
        new_car = Car(brand = brand_, model = model_, init_odo = odo_, current_odo=odo_, odo_unit = unit_)
        db.session.add(new_car)
        db.session.commit()
        
    return render_template("add_car.html")