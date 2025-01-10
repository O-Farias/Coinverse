import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def convert_currency(from_currency, to_currency, amount):
    """Consulta a API para converter moedas."""
    response = requests.get(f"{API_URL}{from_currency}")
    if response.status_code != 200:
        raise Exception("Erro ao acessar a API de conversão.")

    rates = response.json()["rates"]
    if to_currency not in rates:
        raise Exception("Moeda de destino não suportada.")

    rate = rates[to_currency]
    result = amount * rate
    return result, rate
