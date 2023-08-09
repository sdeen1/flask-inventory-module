from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Regexp, NumberRange

class AddItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired(message="Item name is required")])
    description = TextAreaField('Item Description')
    total = IntegerField('Total Number of Items', validators=[NumberRange(min=0, message="Total inventory of item is required.")])
    halfDay = StringField('Half Day', validators=[Regexp('^\s*\d*\s*$', message="Must be blank or a number")])
    day = StringField('Day', validators=[Regexp('^\s*\d*\s*$', message="Must be blank or a number")])
    week = StringField('Week', validators=[Regexp('^\s*\d*\s*$', message="Must be blank or a number")])
    month = StringField('Month', validators=[Regexp('^\s*\d*\s*$', message="Must be blank or a number")])
    submit = SubmitField('Submit')