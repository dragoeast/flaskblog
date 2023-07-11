import os
import secrets
from PIL import Image
from flask import url_for
from flaskblog import app, mail

from flask_mail import Message


def save_picture(form_picutre):
    random_hex = secrets.token_hex(8)
    _file_name, file_extention = os.path.splitext(form_picutre.filename)
    picture_filename = random_hex + file_extention
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename)
    
    output_size = (125, 125)
    image = Image.open(form_picutre)
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_filename

def send_reset_email(user):
    token = user.get_reset_token(expires_sec=900)
    message = Message(subject='Password Reset Request',
                      sender='noreply@demo.com',
                      recipients=[user.email])
    message.body = f'''
To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(message=message)
    
