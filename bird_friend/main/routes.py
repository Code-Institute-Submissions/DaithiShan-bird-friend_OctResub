from flask import (
    render_template, redirect, url_for, Blueprint, request, flash, current_app)
from flask_login import current_user
from bird_friend.models import Bird

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Route for visitors not yet logged in or
    signed up to the photo-sharing app
    """
    if current_user.is_authenticated:
        # redirect users to main page if they are already registered
        return redirect(url_for('main.gallery'))
    return render_template('main/index.html')


@main.route('/gallery')
def gallery():
    birds = Bird.objects()
    return render_template('main/gallery.html', title="Gallery", birds=birds)
