import alpaca_trade_api as tradeapi
import numpy as np
import time
import os
from dotenv import load_dotenv

load_dotenv()

api = tradeapi.REST(
    key_id=os.getenv('PUB_KEY'), 
    secret_key=os.getenv('SEC_KEY'), 
    base_url='https://paper-api.alpaca.markets' # This is the URL for paper trading, for real trading, don't enter a base_url
) 

pos_held = False

def log_trade(**trade_data):
    print("i traded")

def place_buy_order(symbol):
    trade_data = {
        'symbol': symbol,
        'qty': 1,
        'side': 'buy',
        'type': 'market',
        'time_in_force': 'gtc'
    }
    api.submit_order(**trade_data)
    log_trade(**trade_data)
    
def place_sell_order(symbol):
    trade_data = {
        'symbol': symbol,
        'qty': 1,
        'side': 'sell',
        'type': 'market',
        'time_in_force': 'gtc'
    }
    api.submit_order(**trade_data)
    log_trade(**trade_data)

def get_market_data(symbol):
    print("")
    print("Retreiving weekly & monthly moving averages...")
    days = 30
    timeframe = tradeapi.TimeFrame(1, tradeapi.TimeFrameUnit['Day'])

    # Get one bar object for each of the past 30 days
    market_data = api.get_bars(symbol, timeframe, limit=days) 
    
    # This array will store all the closing prices from the last 30 days
    # bar.c is the closing price of that bar's time interval
    close_list = [] 
    for bar in market_data[symbol]:
        close_list.append(bar.c) 
    
    # Convert to numpy array to easily grab their averages
    close_list = np.array(close_list, dtype=np.float64) 
    weekly_ma = np.mean(close_list[days-7:])
    monthly_ma = np.mean(close_list)
    latest_closing_price = close_list[days - 1]   
    print("Weekly Moving Average: " + str(weekly_ma))
    print("Monthly Moving Average: " + str(monthly_ma))
    print("Latest Closing Price: " + str(latest_closing_price))

    return weekly_ma, monthly_ma, latest_closing_price

def trade_on_moving_average():
    while True:
        symbol = "BTC"
        weekly_ma, monthly_ma, latest_closing_price = get_market_data(symbol)
        
        # If the weekly moving average moves above the monthly, buy
        if weekly_ma > monthly_ma and not pos_held: 
            place_buy_order(symbol)
            pos_held = True
        
        # If the weekly moving average moves below the monthly, sell
        elif weekly_ma < monthly_ma and pos_held: 
            place_sell_order(symbol)
            pos_held = False
        
        # Wait one day before retreiving more market data
        time.sleep(86400) 

trade_on_moving_average()