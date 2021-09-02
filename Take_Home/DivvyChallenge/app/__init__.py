from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # tell Flask application to use SQLAlchemy and Migrate 
    db.init_app(app)
    migrate.init_app(app, db)

    from app.blueprints.main import bp as main
    app.register_blueprint(main)
    return app
