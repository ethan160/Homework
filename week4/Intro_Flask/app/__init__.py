from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.blueprints.blog import bp as blog
    app.register_blueprint(blog)

    with app.app_context():
        # building the reset of the flask application (configurations, additional packages, etc)
        from .import routes # import from current 

    return app

