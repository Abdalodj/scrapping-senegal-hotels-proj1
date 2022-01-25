import requests
import bs4
import time
import json 
import pprint as pp
import traceback

with open("hotels.json", "r+", encoding='utf-8') as hotels, open("hotel_prices.json", "r") as prices:
  list_hotels = json.load(hotels)
  list_prices = json.load(prices)
  hotels.truncate(0)
  for i in range(24):
    del list_hotels[i]["price"]
    print(len(list_prices[i]["options"]))
    list_hotels[i]['priceOptions'] = list_prices[i]["options"]

  json.dump(list_hotels, hotels, indent=2, ensure_ascii=False)