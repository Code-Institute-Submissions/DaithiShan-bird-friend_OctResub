from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length
from bird_friend.models import BirdType


class UploadForm(FlaskForm):
    bird_type = SelectField("Breed",
                        choices=[
                            (bird_type.pk, bird_type.bird_type_name)
                            for bird_type in BirdType.objects],
                        validators=[DataRequired()])
    nickname = StringField("Nickname",
                       validators=[
                           DataRequired(),
                           Length(max=50,
                                  message="Max name length is 50 characters! "
                                          "No space for the full Latin name, sorry!")])
    img_url = FileField("Photo",
                        validators=[FileRequired(),
                                    FileAllowed(['jpg', 'jpeg', 'png'])])
    about = TextAreaField("Tell us about this photo!",
                          validators=[
                              Length(max=300,
                                     message="About section has a max "
                                             "character limit of 300!")])
    submit = SubmitField('Upload')