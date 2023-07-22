from flask import Blueprint, render_template, jsonify
from .db_models import Car, Refuel
from . import db
import json
from datetime import datetime
from flask import request
from sqlalchemy import update

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
        if brand_ and model_ and odo_ and unit_:
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

@views.route('/delete-refuel', methods=['POST'])
def delete_refuel():  
    refuel = json.loads(request.data)
    refuelId = refuel['refuel_id']
    refuel = Refuel.query.get(refuelId)
    if refuel:
        db.session.delete(refuel)
        db.session.commit()

    return jsonify({})

@views.route('/car/<car_id>', methods=['GET', 'POST'])
def car_menage(car_id):
    car = Car.query.get(car_id)
    if(car):
        if request.method == "POST":
            date_ = request.form['date']
            price_ = request.form['price']
            odo_ = request.form['odo']
            amount_ = request.form['amount']
            if date_ and price_ and odo_ and amount_:
                new_refueling = Refuel(car_id = car.id, refuel_odo = odo_, date = datetime.strptime(date_, "%Y-%m-%d"), price = price_, amount = amount_)
                car.current_odo = odo_
                db.session.add(new_refueling)
                db.session.commit()
        return render_template("car_menage.html", car = car)
    else: return render_template('404.html')
    
@views.route('/api/<type>', methods=['GET', 'POST'])
def cars_api(type):
    car_id = request.args.get('id')
    if type == "refuel":
        # refuels for selected car 
        if car_id: 
            refuels  =[]
            for refuel in db.session.query(Refuel).join(Car).filter(Car.id == car_id).all():
                new_refuel = {
                    'id' : refuel.id,
                    'date' : refuel.date,
                    'price' : refuel.price,
                    'amount' : refuel.amount,
                    'refuel_odo' : refuel.refuel_odo,
                }
                refuels.append(new_refuel.copy())
            
            return {'refuels' : refuels}
        else:
            refuels = []
            for refuel in db.session.query(Refuel).join(Car).all():
                new_refuel = {
                    'id' : refuel.id,
                    'date' : refuel.date,
                    'price' : refuel.price,
                    'refuel_odo' : refuel.refuel_odo,
                    'amount' : refuel.amount,
                }
                
                refuels.append(new_refuel.copy())
            
            return {'refuels' : refuels}
    
    else:
        if car_id:
            car = db.session.query(Car).get(car_id)
            if car:
                return {
                        'id' : car.id,
                        'brand' : car.brand,
                        'model' : car.model,
                        'init_odo' : car.init_odo,
                        'current_odo' : car.current_odo,
                        'units' : car.odo_unit,
                    }
            else:
                return render_template("404.html")
            
        elif not car_id and type == 'cars':
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