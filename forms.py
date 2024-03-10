from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators


class CurrencyForm(FlaskForm):
    from_currency = StringField(
        'From Currency', [validators.Length(min=3, max=3), validators.InputRequired()])
    to_currency = StringField('To Currency', [validators.Length(
        min=3, max=3), validators.InputRequired()])
    amount = FloatField('Amount', [validators.InputRequired()])
