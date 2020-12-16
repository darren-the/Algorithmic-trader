# Algorithmic trading (Bitcoin)
## Contents
(write something here)

## Background
The cryptocurrency markets have always fascinated me ever since the boom in 2017. However, it wasn't till recently that
I heard about algorithmic trading, this is essentially a way of automating trades based off some pre-set rules and conditions.
Being my first attempt, I decided to start with the basics by using the well-known moving average (MA) cross strategy. Although I do not really expect this to be profitable by any means, I do wish to gain some insights into the general processes involved in building an algorithmic trader so that I can hopefully build better ones in the future!

## The strategy
The main inspiration for the strategy can be found here: 
<br>
https://www.tradingview.com/chart/EURGBP/1ImcwzBC-The-Simplest-Scalping-Strategy-With-3-EMA-s-For-20-Pips-Per-Day/

Here are the main points:
* Buy when the 5 MA crosses from below the 20 MA to above it but only if both the 5 MA and 20 MA are above the 50 MA.
* Sell when the 5 MA crosses from above the 20 MA to below it but only if both the 5 MA and 20 MA are below the 50 MA.

The diagram below demonstrates an example of a successful short.
<br>
<img src="images/short_pos3.png" width="800">

## Method

### 1. Gathering the data
The first step is to gather historical data so that we can backtest our algorithm with it in the future. To do this, I will use the Bitfinex API to request data from their public candles endpoint. Here is a sample of some code for a basic request. See the full code [here](https://github.com/darren-the/Algorithmic-trader/blob/master/gather_candles.ipynb)
```
import requests

domain = "https://api-pub.bitfinex.com/v2/"
path = "candles/trade:1m:tBTCUSD/hist"
start = -1  # the start timestamp
end = -1  # the end timestamp
payload = {'limit': 10000, 'start': start, 'end': end, 'sort': 1}
try:
    r = requests.get(domain + path, params=payload).json()
except:
    raise Exception("Error.")
```

### 2. Calculating moving averages
After successfully gathering the historical candlestick data, the next step is to calculate the moving average price at the close of each candle. For this particular algorithm we will calculate the 5, 20 and 50 moving averages. Calculating these are quite simple, all we need to do is take the arithmetic mean of the last n closing prices at each point.
For example, if the last 5 closing prices were 10, 15, 20, 30 and 25, then the 5 MA can be calculated like the following: (10 + 15 + 20 + 30 + 25) / 5 = 20. The full code for this section can be found [here](https://github.com/darren-the/Algorithmic-trader/blob/master/gather_mavg.ipynb)

More information on moving averages can be found [here](https://www.investopedia.com/terms/m/movingaverage.asp)

### 3. Backtesting the algorithm


## Results
(write something here)

## Conclusion
(write something here)
