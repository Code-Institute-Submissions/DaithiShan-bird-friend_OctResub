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
    form = RegisterForm()
    # Customised register function from Code Institute Walkthrough Project
    if request.method == "POST" and form.validate_on_submit():
        user = User(username=form.username.data.lower(), email=form.email.data)
        user.set_password(form.password.data)
        user.save()
        login_user(user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

    return render_template("user/register.html", title="Register", form=form)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
