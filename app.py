from flask import Flask
import pytest
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'     
db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    brand = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(30), nullable = False)
    
    def __repr__(self):
        return f"{self.brand} {self.model}"

@app.route('/')
def index():
    return "hello world"