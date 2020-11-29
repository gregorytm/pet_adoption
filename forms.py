from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, NumberRange, Optional

class PetForm(FlaskForm):

    name = StringField("Pet name", validators=[InputRequired(message="name can not be empty")])
    species = SelectField("Species", choices=[('dog', 'Dog'), ('cat', 'Cat'), ('pine', 'Porcupine')])
    photo_url = StringField("Pet image", validators=[Optional(), URL()])
    age = FloatField("Pet age", validators=[Optional(), NumberRange(min=1, max=30, message="Age must be between 1 and 30")])
    notes = StringField("Notes")
    is_available = BooleanField("Currently available")