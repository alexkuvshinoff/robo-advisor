# app/robo_advisor.py

import csv
import json
import os

from dotenv import load_dotenv
import requests

def to_usd(my_price):
        return "${0:,.2f}".format(my_price)
# 
# INFO INPUTS
#
api_key = os.environ.get("ALPHAVANTAGE_API_KEY") 

symbol = input("Please input a Stock Ticker: ") #TODO: accept user input

# what if there is no symbol
if symbol == None or symbol.isdigit():
    print("Whoops, there isn't a stock with that ticker, please try another one!")
    exit()

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

if 'Error Message' in parsed_response:
    print("Whoops, there isn't a stock with that ticker, please try another one!")
    exit()

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0] # TODO: assumes first day is on top but consider sorting to ensure latest day is first

latest_close = tsd[latest_day]["4. close"]

# get high price from each day
high_prices = []
low_prices = []
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

# csv_file_path = "data/prices.csv" # a relative filepath
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    # looping
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date, 
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
            })

x = latest_close 
y = recent_low + (recent_low * .2)

def recommendation(x, y):
    if (float(x) < y):
        return "BUY!"
    else:
        return "DON'T BUY!"

a = "BECAUSE THE STOCK'S LATEST CLOSING PRICE IS LESS THAN 20% OF IT'S RECENT LOW"
b = "BECAUSE THE STOCK'S LATEST CLOSING PRICE IS MORE THAN OR EQUAL TO 20% OF IT'S RECENT LOW"

def because(x, y):
    if (float(x) < y):
        return a
    else:
        return b

print("-------------------------")
print("SELECTED SYMBOL: " + symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: " + recommendation(x, y))
print("BECAUSE: " + because(x, y))
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("HAPPY INVESTING!")
print("-------------------------")


# If the stock's latest closing price is less than 20% above its recent low, "Buy", else "Don't Buy".
