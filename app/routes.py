from flask import render_template, request
from app import app
from app.converter import convert_currency

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form.get('from_currency').upper()
    to_currency = request.form.get('to_currency').upper()
    amount = float(request.form.get('amount'))

    try:
        result, rate = convert_currency(from_currency, to_currency, amount)
        return render_template('result.html', from_currency=from_currency, to_currency=to_currency, amount=amount, result=result, rate=rate)
    except Exception as e:
        return render_template('result.html', error=str(e))
