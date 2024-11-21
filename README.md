## Porphyrios: The AI-Enabled Trading Bot

The goal of this project is to set up a bot to trade various stocks and cryptocurrencies automatically based on the recommendations of Llama 3.2, leveraging Alpaca's API for market data and to issue buy and sell orders.

The project is written in Python 3 to more easily leverage opensource LLM models and Alpaca together.

### Version 1

V1 will be a simple algorithm without any AI implementation.

Goals:

1. Buy and sell a single stock/coin based on it's daily moving average.
2. Buy when the price crosses above it.
3. Sell when the price crosses below it.
4. Log operations and calculate tax.

Research:

To begin with, I need to look up a few trading strategies and select the one I want to use.

Trading Strategies:

1. "Swing" Trading: Holding positions based on some indicator for days to weeks
   Pros: can take advantage of larger moves
   Cons: overnight moves down can loose more money, so position sizes are usually smaller
   Buy:
   when a short term moving average crosses above a longer term one,
   when RSI or MACD do something
   Sell: when the short term MA crosses below long term's
2. Day Trading: Buying an asset in the morning and selling during the day if up a certain %
   Pros: consistent income (if market trending up), safer
   Cons: might rack up commissions and miss out on larger movements
   Buy: in the morning basically
   Sell: when/if it goes up to your target or at day's end
3. Scalping: Doing many trades over the day to make little bits at a time
   Pros: possibly safer than day trading since it takes advantage of smaller swings
   Cons: fees add up and seems schizo
   Buy:
   Sell:
4. Position Trading: holding an asset for weeks to years waiting for larger price movements
   Pros: get-rich-quick
   Cons: money deployed on positions may be inaccessible for extended durations
   Buy:
   Sell:
5. Breakout Trading: buying an asset as it breaks above a long-term resistance level and riding its momentum up to some set percentage gain
   Pros:
   Cons:
   Buy:
   Sell:
6. Reversal Trading: buying an asset as it begins to rise from a long-term slump and riding the momentum up to a certain level
   Pros:
   Cons:
   Buy:
   Sell:
7. Momentum Trading: buying assets that exibit strong upward movements and selling when it appears the enthusiasm is waning
   Pros:
   Cons: Crab & bear markets trigger it's stop losses more
   Buy:
   Sell:

Assets:

Commodities (Futures),
Crypto,
Stocks

Selection:

To begin somewhere, I think swing trading or position trading fit my risk tolerance.
Probably start with crypto swing trading. Look up TA techniques used by other swing traders
and try to convert them to code to auto-buy/sell something for V1.

For a simple entry to autotrading, I checked out a bitcoin chart with a 7-day MA and 30-day.
While it doesn't always work 100%, it seemed like if I buy when the weekly MA moves above the monthly, it makes a profit if I sell when it falls below.

It does mean though that I'd be holding positions for up to 2 months it seems like. Which is fine as long as I'm holding/tracking multiple assets.

### Version 2

V2 will begin using Llama 3.2 or a similar LLM. It will be fed recent market data and be asked to make a decision to buy or sell a given asset.

Maybe do a daily or weekly review of all available assets to inspect whether they're close to resistance levels or if their momentum has changed to allow the AI to make decisions
