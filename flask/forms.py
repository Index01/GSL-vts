

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class TagForm(FlaskForm):
    name = StringField('Radio Handle', validators=[DataRequired()])
    tagID = StringField('RFID tag number', validators=[DataRequired()])

class HiddenForm(FlaskForm):
    hiddenTagID = HiddenField('hiddenTagID', validators=[DataRequired()])
    hiddenUTCField = HiddenField('utc', validators=[DataRequired()])

