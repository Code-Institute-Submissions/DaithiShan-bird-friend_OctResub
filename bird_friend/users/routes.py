import os
from flask import (
    flash, render_template, redirect, request, url_for, Blueprint)
from flask_login.utils import login_required
from mongoengine.errors import DoesNotExist
from bird_friend import db
from bird_friend.users.forms import (
    RegisterForm, LoginForm, EditProfileForm, DeleteAccountForm)
from bird_friend.models import User, Bird
from flask_login import current_user, login_user, logout_user
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
if os.path.exists("env.py"):
    import env

users = Blueprint('users', __name__)


@users.route('/login', methods=['GET', 'POST'])
def login():
    """route for logging in users"""
    if current_user.is_authenticated:
        return redirect(url_for('main.gallery', view='popular', animate='on'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            user = User.objects.get(username=form.username.data.lower())
        except DoesNotExist:
            user = None
        # If user doesn't exist or password doesn't match, notify user and
        # reload page
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'exclamation')
            return redirect(url_for('users.login'))
        # else login the user and redirect
        login_user(user)
        flash(f'Welcome back, {user.username}!', 'check-circle')
        next_page = request.args.get('next')
        # If the user had pressed to go to a page behind a @login_required
        # Then redirect to that 'next' page, otherwise go to main gallery
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.gallery', view='popular', animate='on')
        return redirect(next_page)
    # 'GET' functioning
    return render_template('user/login.html', title="Login", form=form)


@users.route('/logout')
def logout():
    """route to log out current user"""
    logout_user()
    return redirect(url_for('main.index'))


@users.route("/register", methods=["GET", "POST"])
def register():
    # route for registering new users
    if current_user.is_authenticated:
        # redirect users to main page if they are already registered
        return redirect(url_for('main.gallery', view='popular', animate='on'))
    form = RegisterForm()
    # Customised register function from Code Institute Walkthrough Project
    if request.method == "POST" and form.validate_on_submit():
        user = User(username=form.username.data.lower(), email=form.email.data)
        user.set_password(form.password.data)
        user.set_avatar(
            f'https://res.cloudinary.com/the-mater-foundation/image/upload/v1626200015'
            f'/bird_friend/avatars/bird{randint(1, 12)}.jpg')
        user.save()
        login_user(user)
        flash("Registered! Please choose an avatar", 'check-circle')
        # Redirect to select avatar
        return redirect(url_for('users.select_avatar'))
    # 'GET' functionality
    return render_template('user/register.html', title="Register", form=form)


@users.route('/profile/<username>')
def profile(username):
    """
    Route for displaying a user's profile page
    displaying photos they've taken, and photos they've favourited
    """
    user = User.objects(username=username).first()
    user_birds = Bird.objects(uploader=user)
    favourites = Bird.objects(faved_by__contains=user.id)
    return render_template('user/profile.html', title=f"{user.username}",
                           user=user, user_birds=user_birds, favourites=favourites)


@users.route('/select_avatar')
@login_required
def select_avatar():
    """route for selecting avatar for new users
        or editing avatar for current users"""

    # Fuctioning if user has selected a new avatar
    if request.args.get('selected'):
        user = User.objects.get(username=current_user.username)
        user.set_avatar(request.args.get('selected'))
        user.save()
        flash('Your avatar has been updated!', 'check-circle')
        return redirect(
            url_for('users.profile', username=current_user.username))
    # Default functioning to present available avatars
    avatars = [
        f'https://res.cloudinary.com/the-mater-foundation/image/upload/v1626200015'
        f'/bird_friend/avatars/bird{i}.jpg'
        for i in range(1, 13)]
    return render_template('user/select_avatar.html', avatars=avatars,
                           title='Choose Avatar')


@users.route('/edit_profile/<user_id>', methods=['GET', 'POST'])
@login_required
def edit_profile(user_id):
    """route for editing username, email
    or password"""
    user = User.objects(pk=user_id).first()
    if user != current_user and current_user.username != 'admin':
        flash("You cannot edit someone else's profile!", "exclamation")
        return redirect(url_for('main.gallery', view='popular'))
    form = EditProfileForm()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.save()
        flash('Account updated successfully!', 'check-circle')
        return redirect(url_for('users.profile', username=user.username))
    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
    return render_template('user/edit_profile.html', title='Edit Profile',
                           user=user, form=form)


@users.route('/delete_account/<user_id>', methods=['GET', 'POST'])
@login_required
def delete_account(user_id):
    """route for editing username, email
    or password"""
    user = User.objects(pk=user_id).first()
    if user != current_user and current_user.username != 'admin':
        flash("You cannot delete someone else's profile!", "exclamation")
        return redirect(url_for('main.gallery', view='popular'))
    form = DeleteAccountForm()
    if form.validate_on_submit():
        # Complete password check before deletion (admin can enter admin
        # password)
        if not current_user.check_password(form.password.data):
            flash('Invalid Password', 'exclamation')
            return redirect(url_for('users.profile', username=user.username))
        else:
            if current_user.username != 'admin':
                # Logout user to home screen
                logout_user()
            # Delete stored cloudinary image for each of user's photos
            birds = Bird.objects(uploader=user)
            for bird in birds:
                bird.delete_bird_image(user.username, bird.pk)
            # Delete user (which will cascade delete birds, comments, etc)
            user.delete()
            flash('Account deleted! Hope to see you again', 'check-circle')
            return redirect(url_for('main.index'))

    return render_template('user/delete_account.html', user=user,
                           title='Delete Account', form=form)


@users.route('/favourite/<bird_id>')
@login_required
def favourite(bird_id):
    """
    Route for saving a photo to the current
    user's favourites
    """
    bird = Bird.objects(pk=bird_id).first_or_404()
    # Remove from favourites if already favourited
    if current_user in bird.faved_by:
        bird.update(pull__faved_by=current_user.id)
        bird.update(dec__favourites=1)
    elif bird.uploader == current_user:
        flash(f"You can't favourite your own photo, but it's gorgeous!", 'exclamation')
        return request.referrer
    # else add to favourites
    else:
        bird.update(push__faved_by=current_user.id)
        bird.update(inc__favourites=1)
        flash(f"{bird.nickname} added to your favourite photos!", 'check-circle')

    # Return to previous page
    return redirect(request.referrer)
