from bird_friend import db
from werkzeug.security import generate_password_hash, check_password_hash
from mongoengine import CASCADE
from flask_login import UserMixin
from flask import current_app
from bird_friend import login
from cloudinary import uploader
import os

# App models from student project - 
#https://github.com/cjcon90/hot-dogz/blob/main/hot_dogz/users/forms.py  

class User(UserMixin, db.Document):
    username = db.StringField(max_length=12, unique=True, required=True)
    email = db.EmailField(max_length=100, unique=True, required=True)
    password_hash = db.StringField(required=True)
    img_url = db.URLField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class BirdType(db.Document):
    birdtype_name = db.StringField(required=True)

    def __repr__(self):
        return f"Bird Type:('{self.birdtype_name}')"


class Bird(db.Document):
    bird_type = db.ReferenceField(BirdType)
    nickname = db.StringField(max_length=50, required=True)
    img_url = db.URLField()
    img_url_card = db.URLField()
    img_url_thumb = db.URLField()
    about = db.StringField(max_length=250,
                           default="No backstory to this photo yet!")
    uploader = db.ReferenceField(User, reverse_delete_rule=CASCADE)
    upload_date = db.DateTimeField(default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Bird Type('{self.birdtype_name}', uploader = {self.uploader.username})"

    def set_bird_image(self, bird_img, user, pk):
        # Get an individual folder for each user's photo uploads
        # and set filename to bird's primary key,
        # so a new photo upload overwrites the old one
        public_id = f"bird_friend/{user}/{pk}"
        # upload image to identified folder
        # with eager transformations for smaller image
        res = uploader.upload(bird_img, public_id=public_id, overwrite=True)
        # Get already configurated cloud name
        cloud_name = os.environ.get("CLOUD_NAME")
        # add to URL for building URL
        endpoint = f"https://res.cloudinary.com/{cloud_name}/image/upload"
        # Add transformations for delivering lower quality, smaller version
        # for dog card and dog profile page respectively
        card_transformation = '/c_fill,g_auto,h_350,w_525,q_auto:low'
        thumb_transformation = '/w_500,c_scale,q_auto:low'
        # Get the version, id and format details from uploaded image
        version = f"/v{res['version']}/"
        public_id = res["public_id"]
        image_format = res["format"]
        # add links for full quality image and thumbnails to Dog model
        self.img_url = f"{endpoint}{version}{public_id}.{image_format}"
        self.img_url_card = f"{endpoint}{card_transformation}" \
                            f"{version}{public_id}.{image_format}"
        self.img_url_thumb = f"{endpoint}{thumb_transformation}" \
                             f"{version}{public_id}.{image_format}"

   def delete_bird_image(self, user, pk):
        public_id = f"bird_friend/{user}/{pk}"
        uploader.destroy(public_id)


@login.user_loader
def load_user(id):
    return User.objects.get(pk=id)