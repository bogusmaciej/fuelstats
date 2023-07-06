from flask import Blueprint, render_template, jsonify
from .db_models import Car, Refuel
from . import db
import json
from flask import request

views = Blueprint("views", __name__)

@views.route("/", methods = ['POST', 'GET'])
def index():
    return render_template("show_cars.html")

@views.route("/add_car", methods = ['POST', 'GET'])
def add():
    if request.method == "POST":
        brand_ = request.form['brand']
        model_ = request.form['model']
        odo_ = request.form['odo']
        unit_ = request.form['unit']
        # if brand_ and model_ and odo_ and unit_:
        new_car = Car(brand = brand_, model = model_, init_odo = odo_, current_odo=odo_, odo_unit = unit_)
        db.session.add(new_car)
        db.session.commit()
            
        
    return render_template("add_car.html")

@views.route('/delete-car', methods=['POST'])
def delete_car():  
    car = json.loads(request.data)
    carId = car['car_id']
    car = Car.query.get(carId)
    if car:
        db.session.delete(car)
        db.session.commit()

    return jsonify({})

@views.route('/car/<car_id>', methods=['GET', 'POST'])
def car_menage(car_id):
    car = Car.query.get(car_id)
    if(car):
        return render_template("car_menage.html", car = car)
    else: return render_template('404.html')
    
@views.route('/api/<type>', methods=['GET', 'POST'])
def cars_api(type):
    if type == 'cars':
        cars = []
        
        for car in db.session.query(Car).all():
            new_car = {
                'id' : car.id,
                'brand' : car.brand,
                'model' : car.model,
                'init_odo' : car.init_odo,
                'current_odo' : car.current_odo,
                'units' : car.odo_unit,
            }
            
            cars.append(new_car.copy())
        
        return {'cars' : cars}