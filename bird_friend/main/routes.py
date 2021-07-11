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
    return render_template('main/index.html')


# @main.route(/gallery/<view>)
# def gallery(view):
#     """
#     Route for main gallery page with sections to
#     display bird photos sorted and filtered by:
#     Popular: most liked photos uploaded recently
#     New: The most recently uploaded photos
#     """
#     page = request.args.get("page", 1, type=int)
#     if view == 'popular':
#         birds = Bird.objects.order_by('-likes', '-upload_date').paginate(
#             page=page, per_page=6)
#     elif view == 'new':
#         birds = Bird.objects.order_by('-upload_date').paginate(
#             page=page, per_page=6)
#     animate = request.args.get('animate')
#     return render_template('main/gallery.html', title="Gallery", birds=birds,
#                            view=view, animate=animate)