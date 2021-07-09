import os
from flask import flash, render_template, redirect, request, url_for, Blueprint
from mongoengine.errors import DoesNotExist
from bird_friend import db
from bird_friend.users.forms import RegisterForm
from bird_friend.models import User
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

users = Blueprint('users', __name__)

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
