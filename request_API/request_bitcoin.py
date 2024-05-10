import requests

url = 'https://api.binance.com/api/v3/ticker/price'
try:
    responce = requests.get(url, params={'symbol': 'BTCUSDT'})

    price_object = responce.json()
    price = float(price_object['price'])
    print(price)
except requests.exceptions.ConnectionError as err:
    print(f"ZOV ZOV: {error}")