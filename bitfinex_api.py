import requests
import time
from progress import PBar

domain = "https://api-pub.bitfinex.com/v2/"

tLength = {'1m': 60000, '5m': 300000, '15m': 900000, '30m': 1800000, '1h': 3600000, '3h': 10800000, '6h': 21600000, 
    '12h': 43200000, '1D': 86400000, '7D': 604800000, '14D': 1209600000}

def fetch_hist(symbol, timeframe, start, end):
    """
    Sends a get request(s) for historical data using the given parameters 
    and returns the result as a list.

    Params:
    - symbol: The symbol you want information about (string). E.g. 'BTCUSD', 'ETHUSD', 'USD', 'BTC'
    - timeframe: (string) '1m', '5m', '15m', '30m', '1h', '3h', '6h', '12h', '1D', '7D', '14D'
    - start: The starting timestamp in ms (float)
    - end: The ending timestamp in ms (float)
    """

    data = []
    block_size = 10000
    pbar = PBar(num_candles(start, end, timeframe))

    # Fetching data in blocks of size: 10000
    while start < end:
        time.sleep(1)
        a, b = max_range(start, end, timeframe, block_size)
        candles = req_hist(symbol, timeframe, a, b)
        for candle in candles:
            list_to_float(candle)
            pbar.update()
            if candle[0] < end:
                data.append(candle)
        start = float(b)
    pbar.terminate()
    return data

def req_hist(symbol, timeframe, start, end):
    """
    Sends a get request for historical data using the given parameters 
    and returns the result in json format.

    Params:
    - symbol: The symbol you want information about (string). E.g. 'BTCUSD', 'ETHUSD', 'USD', 'BTC'
    - timeframe: (string) '1m', '5m', '15m', '30m', '1h', '3h', '6h', '12h', '1D', '7D', '14D'
    - start: The starting timestamp in ms (float)
    - end: The ending timestamp in ms (float)
    """
    path = "candles/trade:" + timeframe + ":t" + symbol + "/hist"
    payload = {'limit': 10000, 
                'start': start, 'end': end, 'sort': 1}
    try:
        return requests.get(domain + path, params=payload).json()
    except:
        raise Exception("Invalid request.")

def max_range(start, end, t, _max=10000):
    diff = int((float(end) - float(start)) / tLength[t])
    if diff > _max:
        end = float(start) + tLength[t] * _max
    return str(start), str(end)

def list_to_float(_list):
    for i in range(len(_list)):
        _list[i] = float(_list[i])

def num_candles(start, end, t):
    return round((end - start) / tLength[t])
