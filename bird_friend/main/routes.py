from flask import (
    render_template, redirect, url_for, Blueprint, request, flash, current_app)
from flask_login import current_user
from bird_friend.models import Bird
from bird_friend.main.forms import ContactForm
from bird_friend.main.utils import send_email

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Route for visitors not yet logged in or
    signed up to the photo-sharing app
    """
    if current_user.is_authenticated:
        # redirect users to main page if they are already registered
        return redirect(url_for('main.gallery', view='popular', animate='on'))
    return render_template('main/index.html')


@main.route('/gallery/<view>')
def gallery(view):
    """
    Route for main gallery page with sections to
    display birds sorted and filtered by:
    Popular: most liked photos uploaded recently
    New: most recently uploaded photos
    """
    page = request.args.get("page", 1, type=int)
    if view == 'popular':
        birds = Bird.objects.order_by('-favourites').paginate(
            page=page, per_page=6)
    elif view == 'new':
        birds = Bird.objects.order_by('-upload_date').paginate(
            page=page, per_page=6)
    animate = request.args.get('animate')
    return render_template('main/gallery.html', title="Gallery", birds=birds,
                           view=view, animate=animate)


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_email(subject='[Bird Friend] Contact Form Submission',
               sender=current_app.config['ADMINS'][0],
               recipients=[current_app.config['ADMINS'][1]],
               text_body=render_template('email/contact_message.txt',
                                         email=form.email.data,
                                         msg=form.message.data),
               html_body=render_template('email/contact_message.html',
                                         email=form.email.data,
                                         msg=form.message.data))
        flash("Thank you! Your message has been sent", "check-circle")
        return redirect(url_for('main.gallery', view='popular'))
    elif request.method == 'GET':
        return render_template('main/contact.html', form=form, title="Contact Us")

