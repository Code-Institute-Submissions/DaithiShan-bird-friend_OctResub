from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login.utils import login_required
from bird_friend.dogs.forms import UploadForm
from flask_login import current_user
from bird_friend.models import Bird, BirdType

birds = Blueprint('birds', __name__)


@dogs.route('/upload_dog', methods=['GET', 'POST'])
@login_required
def upload_bird():
    """
    Route for uploading a photo of a bird to the database
    """
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Upload bird
        bird = Bird(name=form.name.data, uploader=current_user.id,
                  bird_type=form.bird_type.data, about=form.about.data
                  )
        bird.save()
        # Set bird image url to be bird's primary key, for easy deletion and
        # overwriting
        bird.set_bird_image(form.img_url.data, current_user.username, dog.pk)
        bird.save()
        flash('Photo Uploaded!', 'bird')
        return redirect(
            url_for('main.index', title='Bird Friend'))
    # 'GET' functionality
    return render_template('bird/upload_bird.html', form=form,
                           title="Upload Bird")