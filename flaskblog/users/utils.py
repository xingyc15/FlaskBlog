import os
import secrets
from flaskblog import mail
from PIL import Image
from flask_mail import Message
from flask import url_for, current_app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics/', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@qq.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{ url_for('users.reset_token', token=token, _external=True) }

If you did not make this request, just ignore this email.
'''
    mail.send(msg)

# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed
# from flask_login import current_user
# from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
# from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# from flaskblog.models import User

# import secrets
# import os
# from PIL import Image
# from flask import render_template, url_for, flash, redirect, request, abort
# from flaskblog import app, db, bcrypt, mail
# from flaskblog.forms import (RegistrationForm, LoginForm, UpdateAccountForm, PostForm,
#                              RequestResetForm, ResetPasswordForm)
# from flaskblog.models import User, Post
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_mail import Message
