import requests
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import sys

# --- News Data --- #
data = requests.get("https://api.marketaux.com/v1/news/all?symbols=AMZN&filter_entities=true&language=en&api_token=tbHSLMUzhFDWyYv1DQYBNTCzcNtaluErsdP9koPk")

Headline1 = data.json()["data"][0]["description"]
Headline2 = data.json()["data"][1]["description"]
Headline3 = data.json()["data"][2]["description"]
news = [Headline1, Headline2, Headline3]
for headline in news:
        print(f"---> {headline}")

quantity = 0.04363763309 #make variable later

# --- Trading and Orders --- #

trading_client = TradingClient('api-key', 'secret-key', paper=True)
account = trading_client.get_account()
order = "buy"  #make variable later

def sellOrder():
    market_order_data = MarketOrderRequest(
                    symbol="AMZN",
                    qty=quantity,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY
                    )
    return market_order_data

def buyOrder():
    market_order_data = MarketOrderRequest(
                    symbol="AMZN",
                    qty=quantity,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )
    return market_order_data

if order == "sell":
    buyorsell = sellOrder()
elif order == "buy":
    buyorsell = buyOrder()

def submitOrder():
    # Market order

    market_order = trading_client.submit_order(order_data=buyorsell)
    return True, market_order



