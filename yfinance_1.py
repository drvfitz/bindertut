import yfinance as yf

aapl= yf.Ticker("aapl")
aapl

# show actions (dividends, splits)
apple.actions

# show dividends
apple.dividends

# show splits
apple.splits

aapl_historical = aapl.history(start="2020-06-02", end="2020-06-07", interval="1m")
aapl_historical

data = yf.download("AMZN AAPL GOOG", start="2017-01-01", end="2017-04-30")
data
#Will ouptus as OHLC data per ticker first

data = yf.download("AMZN AAPL GOOG", start="2017-01-01",
                    end="2017-04-30", group_by='tickers')
data


aapl = yf.Ticker("aapl")
aapl.info['forwardPE']
aapl.info['dividendRate']

#For a series of dividend events:
aapl.dividends


