import requests
import bs4
import time
import json 
import pprint as pp
import traceback

list_name = []

with open("restaurants.json", encoding='utf-8') as restau_dkF:
  datas = json.load(restau_dkF)
  for data in datas:
    list_name.append(data["name"].split(' '))

  print(len(list_name))
  pp.pprint(list_name)