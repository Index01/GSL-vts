

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TagForm(FlaskForm):
    name = StringField('Radio Handle', validators=[DataRequired()])
    tagID = StringField('RFID tag number', validators=[DataRequired()])

