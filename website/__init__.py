from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db_name = 'database.db'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qweqwe'

    from .views import views
    app.register_blueprint(views, url_prefix="/")
    
    from .db_models import Car, Refuel
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)
    create_db(app)
            
    return app
    
    
def create_db(app):
    if not path.exists(f'website/instance/{db_name}'):
        with app.app_context():
            db.create_all()