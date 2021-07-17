from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from config import Config
from flask_mail import Mail

db = MongoEngine()
login = LoginManager()
# configure view and message when users attempt to access a
# view for which @login_required
login.login_view = 'users.login'
login.login_message = 'You must be logged in to do that!'
login.login_message_category = 'exclamation'

# __init__.py inspired by Corey Schafer YouTube Series on Flask Apps and Blueprints 
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/11-Blueprints

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login.init_app(app)

    from bird_friend.users.routes import users
    from bird_friend.birds.routes import birds
    from bird_friend.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(birds)
    app.register_blueprint(main)

    return app
    