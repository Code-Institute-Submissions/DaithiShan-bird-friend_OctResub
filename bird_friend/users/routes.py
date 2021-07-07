import os
from flask import (
    Flask, flash, render_template,
    redirect, request, url_for, Blueprint)
from mongoengine.errors import DoesNotExist
from bird_friend.users.forms import RegisterForm
from bird_friend.models import User
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm
if os.path.exists("env.py"):
    import env

users = Blueprint('users', __name__)


@users.route("/")
@users.route("/get_birds")
def get_birds():
    birds = mongo.db.birds.find()
    return render_template("birds.html", birds=birds)


@users.route("/register", methods=["GET", "POST"])
def register():
    # Customised register function from Code Institute Walkthrough Project
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
