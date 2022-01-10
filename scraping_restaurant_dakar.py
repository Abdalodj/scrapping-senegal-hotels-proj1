import requests
from bs4 import BeautifulSoup
import time
import traceback
import pprint as pp
import json

restaurants = []




""" url = "https://anaresto.com/liste/?list_type=list"
response = requests.get(url)
if response.ok:
  try:
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    contents = soup.select('.wrapper > a')
    links += [elt['href'] for elt in contents]
  except:
    print([elt.text for elt in contents])
else:
  print('err')

time.sleep(1)

with open('urls_restaurants_dakar.txt', 'w+') as file:
  for link in links:
    file.write(link + '\n') """

with open('urls_restaurants_dakar.txt', 'r') as file, open('restaurants.json', 'w+', encoding="utf-8") as restauJSON:
  count = 0
  for row in file:
    response = requests.get(row.strip('\n'))
    print(response)
    if response.ok:
      restaurant = {
        "name": "",
        "desc": None,
        "category": "restaurant",
        "price": None,
        "mediaUrls": [],
        "services": [],
        "position": {
          "type": "Point",
          "coordinates": [0, 0]
        },
        "address": {
          "address": "Dakar",
          "additional": [],
          "postal": "",
          "coordinates": [0, 0]
        },
        "contact": {
          "phone": [],
          "email": [],
          "url": ""
        },
        "schedule": {
          "lundi": {
            "ouverture": "07:00",
            "fermeture": "23:00",
            "open": True,
            "all": True
          },
          "mardi": {
            "ouverture": "07:00",
            "fermeture": "23:00",
            "open": True,
            "all": True
          },
          "mercredi": {
            "ouverture": "07:00",
            "fermeture": "23:00",
            "open": True,
            "all": True
          },
          "jeudi": {
            "ouverture": "07:00",
            "fermeture": "23:00",
            "open": True,
            "all": True
          },
          "vendredi": {
            "ouverture": "07:00",
            "fermeture": "23:00",
            "open": True,
            "all": True
          },
          "samedi": {
            "ouverture": "07:00",
            "fermeture": "23:00",
            "open": True,
            "all": True
          },
          "dimanche": {
            "ouverture": "07:00",
            "fermeture": "23:00",
            "open": True,
            "all": True
          }
        },
        "score": { "n": 0, "l": 0, "e": [0, 0, 0, 0, 0] },
        "createdAt": None,
        "updatedAt": None
      }
      try:
        soup = BeautifulSoup(response.text, "html.parser")
        restaurant["name"] = soup.select_one('.title > h1').text.strip('\n')
        print(restaurant["name"])
        infos = soup.select('figure > dl > dd')
        if infos[0].text.strip('\nFCFA') != 'Daily menu':
          restaurant["price"] = int(infos[0].text.strip('\nFCFA'))

        if len(infos) > 1:
          restaurant["contact"]["phone"].append(infos[1].text.strip('\n'))

        address = soup.select('address > div')
        if len(address) > 0: restaurant["address"]["address"] = address[0].text.strip('\n')
        if len(address) > 1: restaurant["address"]["additional"] = [address[i].text.strip('\n') for i in range(1, len(address))]

        descriptions = soup.select('article > p')
        b = ['@', '+221', '77', '33', '78', '76']
        restaurant["contact"]["url"] = [elt.text.strip('\n') for elt in descriptions if not any(x in elt.text for x in b) and 'http' in elt.text.strip('\n')]
        b = ['http', '+221', '77', '33', '78', '76']
        restaurant["contact"]["email"] = [elt.text.strip('\n') for elt in descriptions if not any(x in elt.text for x in b) and '@' in elt.text.strip('\n')]
        b = ['+221', '77', '33', '78', '76']
        restaurant["contact"]["phone"] += [elt.text.strip('\n') for elt in descriptions if not any(x in elt.text for x in ['http', '@']) and any(x in elt.text for x in b)]
        b = ['http', '@', '+221', '77', '33', '78', '76']
        restaurant["desc"] = [elt.text.strip('\n') for elt in descriptions if not any(x in elt.text for x in b )]

        hours = soup.select('article > dl > dd')
        schedule = list(restaurant["schedule"].keys())
        size = len(hours)
        for i in range(size):
          strHour = hours[i].text.strip('\n')
          openHour, closeHour = '', ''
          if '–' in strHour:
            openHour, closeHour = strHour.split('–')[0], strHour.split('–')[-1]
          else:
            openHour, closeHour = strHour.split('-')[0], strHour.split('-')[-1]
          restaurant["schedule"][schedule[i]]["ouverture"] = openHour.strip()
          restaurant["schedule"][schedule[i]]["fermeture"] = closeHour.strip()

        images = soup.select('.content > a > img')
        restaurant["mediaUrls"] = [img.get('srcset').split(',')[0] if img.get('srcset') else img.get('src') for img in images]

        services = soup.select('article > ul > li')
        restaurant["services"] = [item.text.strip('\n') for item in services]

        coordBlock = soup.select_one('#page-canvas > #page-content > #map-detail')
        lat = float(coordBlock.get('data-lat'))
        lng = float(coordBlock.get('data-lng'))
        restaurant["position"]["coordinates"] = [lng, lat]
        restaurant["address"]["coordinates"] = [lat, lng]
          
        restaurants.append(restaurant)
      except Exception:
        print(traceback.format_exc())
    else:
      print('err')
    """ break """
    time.sleep(3)

  json.dump(restaurants, restauJSON, indent=2, ensure_ascii=False)

""" pp.pprint(restaurants) """