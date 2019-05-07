import requests
import time
from datetime import datetime

bitcoin_api = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
ifttt_webhook = 'https://maker.ifttt.com/trigger/{}/with/key/{}'
bitcoin_threshold = 6000

while True:
    try:
        key = open('Key.txt','r').readline().rstrip('\n')
        print(key)
        break
    except FileNotFoundError:
        print('Key.txt not found')
        input('Please add Key.txt and press enter')

def get_latest_bitcoin():
    response = requests.get(bitcoin_api)
    response_json = response.json()
    print("got price")
    return float(response_json[0]['price_usd'])


def post_ifttt_webhook(event, value , key):
    data = {'value1':value}
    ifttt_event =  ifttt_webhook.format(event,key)
    requests.post(ifttt_event, json=data)
    print(datetime.now().strftime('%d.%m.%y %H:%M') + " pushed with " + ifttt_event)

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d.%m.%y %H:%M')
        price = bitcoin_price['price']
        row = '{}: <b>{}<b>'.format(date, price)
        rows.append(row)
    return '<br>'.join(rows)

def main():
    bitcoin_history = [];
    while True:
        price = get_latest_bitcoin()
        date = datetime.now()
        bitcoin_history.append({'date' : date, 'price' : price})

        if price >= bitcoin_threshold:
            post_ifttt_webhook('bitcoin_price_emergency', price, key)

        if len(bitcoin_history) == 6:
            post_ifttt_webhook('bitcoin_price_update', format_bitcoin_history(bitcoin_history), key)
            bitcoin_history = []

        time.sleep(5*60)



if __name__ == '__main__':
    main()
