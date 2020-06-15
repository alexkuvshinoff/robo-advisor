# app/robo_advisor.py

import csv
import json
import os

import requests


def to_usd(my_price):
        return "${0:,.2f}".format(my_price)
# 
# INFO INPUTS
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"["3. Last Refreshed"]]

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
    low_price = tsd[date]["2.low"]
    low_prices.append(float(high-Price))

recent_high = max(high_prices)
recent_low = min(high-prices)

# csv_file_path = "data/prices.csv" # a relative filepath
csv_file_path = os.path.join(os.path.dirname(_file_), "..", "data", "prices.csv")

csv_headers = [t"timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    # looping
    writer.writerow({
        "timestamp": "TODO", 
        "high": "TODO"
        "low": "TODO"
        "close": "TODO"
        "volume": "TODO"
        })

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("BECAUSE: TODO")
print("-------------------------")
print("WRITING DATA TO CSV: {csv_file_path}..."")
print("HAPPY INVESTING!")
print("-------------------------")