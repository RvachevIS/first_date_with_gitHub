import requests

url = 'https://api.binance.com/api/v3/ticker/price'

responce = requests.get(url, params={'symbol': 'BTCUSDT'})

price_object = responce.json()
price = float(price_object['price'])
print(price)

