import json
from datetime import datetime

DATABASE_FILE = "conversions.json"

def save_conversion(from_currency, to_currency, amount, result, rate):
    """Salva a conversão no histórico."""
    conversion = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "result": result,
        "rate": rate
    }
    try:
        with open(DATABASE_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(conversion)
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)

def get_conversion_history():
    """Recupera o histórico de conversões."""
    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
