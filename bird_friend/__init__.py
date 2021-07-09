from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from config import Config
from flask_mail import Mail

db = MongoEngine()

# __init__.py inspired by Corey Schafer YouTube Series on Flask Apps and Blueprints 
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/11-Blueprints

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from bird_friend.users.routes import users
    from bird_friend.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(main)

    return app