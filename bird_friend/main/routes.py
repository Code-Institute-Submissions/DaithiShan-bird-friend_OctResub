from flask import (
    render_template, redirect, url_for, Blueprint, request, flash, current_app)
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Route for visitors not yet logged in or
    signed up to the photo-sharing app
    """
    return render_template('main/index.html')