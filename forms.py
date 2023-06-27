from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, DateTimeField, BooleanField, ValidationError
from wtforms.validators import DataRequired, URL, Optional, EqualTo

def password_strength(form, field):
    password = field.data
    # Add your custom password strength validation logic here
    # You can use regular expressions, string length, or other criteria to enforce password strength requirements.
    # For example, you can check if the password contains at least one uppercase letter, one lowercase letter, and one digit.
    if not any(c.isupper() for c in password):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not any(c.islower() for c in password):
        raise ValidationError('Password must contain at least one lowercase letter.')
    if not any(c.isdigit() for c in password):
        raise ValidationError('Password must contain at least one digit.')

class ShowForm(FlaskForm):
    artist_id = StringField(
        'artist_id', 
        validators=[DataRequired()]
    )
    venue_id = StringField(
        'venue_id', 
        validators=[DataRequired()]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(FlaskForm):
    name = StringField(
        'name', 
        validators=[DataRequired()]    
    )
    city = StringField(
        'city', 
        validators=[DataRequired()]   
    )
    state = SelectField(
        'state', 
        validators=[DataRequired()],
        choices = [
            ('AB', 'Abia'),
            ('AD', 'Adamawa'),
            ('AK', 'Akwa Ibom'),
            ('AN', 'Anambra'),
            ('BA', 'Bauchi'),
            ('BY', 'Bayelsa'),
            ('BE', 'Benue'),
            ('BO', 'Borno'),
            ('CR', 'Cross River'),
            ('DE', 'Delta'),
            ('EB', 'Ebonyi'),
            ('ED', 'Edo'),
            ('EK', 'Ekiti'),
            ('EN', 'Enugu'),
            ('FC', 'Federal Capital Territory'),
            ('GO', 'Gombe'),
            ('IM', 'Imo'),
            ('JI', 'Jigawa'),
            ('KD', 'Kaduna'),
            ('KN', 'Kano'),
            ('KT', 'Katsina'),
            ('KE', 'Kebbi'),
            ('KO', 'Kogi'),
            ('KW', 'Kwara'),
            ('LA', 'Lagos'),
            ('NA', 'Nasarawa'),
            ('NI', 'Niger'),
            ('OG', 'Ogun'),
            ('ON', 'Ondo'),
            ('OS', 'Osun'),
            ('OY', 'Oyo'),
            ('PL', 'Plateau'),
            ('RI', 'Rivers'),
            ('SO', 'Sokoto'),
            ('TA', 'Taraba'),
            ('YO', 'Yobe'),
            ('ZA', 'Zamfara')
        ]

    )
    
    address = StringField(
        'address', 
        validators=[DataRequired()]     
    )
    phone = StringField(
        'phone', 
        validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link',
        validators=[Optional(), URL()]
    )
    
    facebook_link = StringField(
        'facebook_link', 
        validators=[Optional(), URL()]
    )
    twitter_link = StringField(
        'twitter_link', 
        validators=[Optional(), URL()]
     )
    
    instagram_link = StringField(
        'instagram_link', 
        validators=[Optional(), URL()]
     )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description', 
        validators=[Optional()]
    )

class ArtistForm(FlaskForm):
    name = StringField(
        'name', 
        validators=[DataRequired()]
    )
   
    phone = StringField(
        'phone', 
        validators=[DataRequired()]
    )
    
    image_link = StringField(
        'image_link', 
        validators=[Optional(), URL()]
    )
    genres = SelectMultipleField(
        'genres', 
        validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
     )
    facebook_link = StringField(
        'facebook_link', 
        validators=[Optional(), URL()]
     )
    
    twitter_link = StringField(
        'twitter_link', 
        validators=[Optional(), URL()]
     )
    
    instagram_link = StringField(
        'instagram_link', 
        validators=[Optional(), URL()]
     )

    seeking_venue = BooleanField( 
        'seeking_venue', 
        validators=[Optional()],
    )

    seeking_description = StringField(
            'seeking_description', 
            validators=[Optional()]
    )

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), password_strength])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), password_strength])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class UserForm(FlaskForm):
    email = StringField(
        'Email', 
        validators=[DataRequired()]
    )