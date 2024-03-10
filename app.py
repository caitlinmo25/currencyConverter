from flask import Flask, render_template, request, flash
import requests
from forms import CurrencyForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '7f77df0840c9cd9a3871119c6c5494dd'

def get_conversion_rate(from_currency, to_currency, amount):
    try:
        access_key ='7f77df0840c9cd9a3871119c6c5494dd'
        response = requests.get(f"http://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}&access_key={access_key}")
        data = response.json()
        return data['result']
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CurrencyForm()
    if form.validate_on_submit():
        from_currency = form.from_currency.data.upper()
        to_currency = form.to_currency.data.upper()
        amount = form.amount.data
        print('helllllo')
        conversion_result = get_conversion_rate(from_currency, to_currency, amount)
        flash(f"The converted amount is {to_currency} {conversion_result:.2f}", 'success')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
