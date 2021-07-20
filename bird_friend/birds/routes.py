from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login.utils import login_required
from bird_friend.birds.forms import UploadForm, EditForm
from flask_login import current_user
from bird_friend.models import Bird, Birdtype

birds = Blueprint('birds', __name__)

# App routes inspired by student project - 
#https://github.com/cjcon90/hot-dogz/blob/main/hot_dogz/users/forms.py 


@birds.route('/upload_bird', methods=['GET', 'POST'])
@login_required
def upload_bird():
    """
    Route for uploading a photo of a bird to the database
    """
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Upload bird
        bird = Bird(nickname=form.nickname.data, uploader=current_user.id,
                  birdtype=form.birdtype.data, about=form.about.data
                  )
        bird.save()
        # Set bird image url to be bird's primary key, for easy deletion and
        # overwriting
        bird.set_bird_image(form.img_url.data, current_user.username, bird.pk)
        bird.save()
        flash('Photo Uploaded!', 'bird')
        return redirect(
            url_for('main.index', title='Bird Friend'))
    # 'GET' functionality
    return render_template('bird/upload_bird.html', form=form,
                           title="Upload Bird")


@birds.route('/bird/<bird_id>', methods=['GET'])
def bird_page(bird_id):
    """
    Route for displaying the a bird's profile page
    """
    bird = Bird.objects(pk=bird_id).first()
    return render_template(
        'bird/bird_page.html', bird=bird, title=f"{bird.nickname}'s Page")

@birds.route('/edit_bird/<bird_id>', methods=['GET', 'POST'])
@login_required
def edit_bird(bird_id):
    """Route for editing a bird's details"""
    bird = Bird.objects(pk=bird_id).first()
    if bird.uploader != current_user and current_user.username != 'admin':
        flash("You cannot edit someone else's photo!", "exclamation")
        return redirect(url_for('main.gallery', view='popular'))
    form = EditForm(birdtype=bird.birdtype.id)
    if form.validate_on_submit():
        # Update Birdtype and About section
        bird.update(nickname=form.nickname.data)
        new_birdtype = Birdtype.objects(pk=form.birdtype.data).first()
        bird.update(birdtype=new_birdtype)
        bird.update(about=form.about.data)
        # If an image is selected, run set image function on Bird model
        if form.img_url.data:
            bird.set_bird_image(form.img_url.data, current_user.username, bird.pk)
        bird.save()
        flash('Updated photo details!', 'check-circle')
        return redirect(url_for('birds.bird_page', bird_id=bird.pk))
    # Pre-fill data for GET requests
    elif request.method == 'GET':
        form.nickname.data = bird.nickname
        form.about.data = bird.about
    return render_template('bird/upload_bird.html', form=form, bird=bird,
                           title="Edit Bird")


@birds.route('/delete_bird/<bird_id>', methods=['GET', 'POST'])
@login_required
def delete_bird(bird_id):
    """Route for deleting a bird from database"""
    bird = Bird.objects(pk=bird_id).first()
    if bird.uploader != current_user and current_user.username != 'admin':
        flash("You cannot delete someone else's photo!", "exclamation")
        return redirect(url_for('main.gallery', view='popular'))
    if request.method == 'POST':
        user = current_user.username
        # Delete bird's image from cloudinary database before deleting bird
        bird.delete_bird_image(user, bird.pk)
        bird.delete()
        flash("Bird photo successfuly deleted", "check-circle")
        return redirect(url_for('users.profile', username=user))
    return render_template('bird/delete_bird.html', bird=bird)