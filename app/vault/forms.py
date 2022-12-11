from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class CredentialForm(FlaskForm):
    website = StringField('Website', validators=[InputRequired(), Length(max=120)])
    username = StringField('Username', validators=[InputRequired(), Length(max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(max=120)])
    submit = SubmitField('Add Credential')

