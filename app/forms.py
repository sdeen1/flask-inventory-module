from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, TextAreaField

class AddItemForm(FlaskForm):
    name = StringField('Item Name')
    description = TextAreaField('Item Description')
    total = IntegerField('Total Number of Items')
    halfDay = FloatField('Half Day')
    day = FloatField('Day')
    week = FloatField('Week')
    month = FloatField('Month')
    submit = SubmitField('Submit')