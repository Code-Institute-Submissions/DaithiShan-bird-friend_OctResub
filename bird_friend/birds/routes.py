from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login.utils import login_required
from bird_friend.birds.forms import UploadForm
from flask_login import current_user
from bird_friend.models import Bird, BirdType

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