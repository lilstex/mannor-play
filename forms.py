from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, DateTimeField, BooleanField, ValidationError
from wtforms.validators import DataRequired, URL, Optional, EqualTo
import pycountry

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
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
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
    genres = SelectMultipleField(
        # TODO implement enum restriction
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
    website_link = StringField(
        'website_link', 
        validators=[Optional(), URL()]
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description', 
        validators=[Optional()]
    )

# class ArtistForm(FlaskForm):
#     country_choices = [(country.alpha_2, country.name) for country in pycountry.countries]
#     state_choices = []
    
#     name = StringField(
#         'name', 
#         validators=[DataRequired()]
#     )
#     city = StringField(
#         'city', 
#         validators=[DataRequired()]
#     )
#     country = SelectField(
#         'country', 
#         validators=[DataRequired()],
#         choices=country_choices
#     )
#     state = SelectField(
#         'state', 
#         validators=[DataRequired()],
#         choices=state_choices
#     )
#     phone = StringField(
#         # TODO implement validation logic for phone 
#         'phone', 
#         validators=[DataRequired()]
#     )
    
#     image_link = StringField(
#         'image_link', 
#         validators=[Optional(), URL()]
#     )
#     genres = SelectMultipleField(
#         'genres', 
#         validators=[DataRequired()],
#         choices=[
#             ('Alternative', 'Alternative'),
#             ('Blues', 'Blues'),
#             ('Classical', 'Classical'),
#             ('Country', 'Country'),
#             ('Electronic', 'Electronic'),
#             ('Folk', 'Folk'),
#             ('Funk', 'Funk'),
#             ('Hip-Hop', 'Hip-Hop'),
#             ('Heavy Metal', 'Heavy Metal'),
#             ('Instrumental', 'Instrumental'),
#             ('Jazz', 'Jazz'),
#             ('Musical Theatre', 'Musical Theatre'),
#             ('Pop', 'Pop'),
#             ('Punk', 'Punk'),
#             ('R&B', 'R&B'),
#             ('Reggae', 'Reggae'),
#             ('Rock n Roll', 'Rock n Roll'),
#             ('Soul', 'Soul'),
#             ('Other', 'Other'),
#         ]
#      )
#     facebook_link = StringField(
#         # TODO implement enum restriction
#         'facebook_link', 
#         validators=[Optional(), URL()]
#      )

#     website_link = StringField(
#         'website_link', 
#         validators=[Optional(), URL()],
#      )

#     seeking_venue = BooleanField( 
#         'seeking_venue', 
#         validators=[Optional()],
#     )

#     seeking_description = StringField(
#             'seeking_description', 
#             validators=[Optional()]
#     )

#     def populate_state_choices(self):
#         country_code = self.country.data
#         try:
#             subdivisions = pycountry.subdivisions.get(country_code=country_code)
#             self.state_choices = [(subdivision.code, subdivision.name) for subdivision in subdivisions]
#         except KeyError:
#             self.state_choices = []

#         self.state.choices = self.state_choices

class ArtistForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    country = SelectField('country', validators=[DataRequired()], choices=[])
    state = SelectField('state', validators=[DataRequired()], choices=[])
    phone = StringField('phone', validators=[DataRequired()])
    image_link = StringField('image_link', validators=[Optional(), URL()])
    genres = SelectMultipleField('genres', validators=[DataRequired()], choices=[
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
    ])
    facebook_link = StringField('facebook_link', validators=[Optional(), URL()])
    website_link = StringField('website_link', validators=[Optional(), URL()])
    seeking_venue = BooleanField('seeking_venue', validators=[Optional()])
    seeking_description = StringField('seeking_description', validators=[Optional()])

    def __init__(self, *args, **kwargs):
        super(ArtistForm, self).__init__(*args, **kwargs)
        self.country.choices = [(country.alpha_2, country.name) for country in pycountry.countries]

    def populate_state_choices(self):
        country_code = self.country.data
        try:
            subdivisions = pycountry.subdivisions.get(country_code=country_code)
            self.state.choices = [(subdivision.code, subdivision.name) for subdivision in subdivisions]
        except LookupError:
            self.state.choices = []

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