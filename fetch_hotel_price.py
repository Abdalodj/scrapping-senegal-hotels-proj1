from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import traceback
import pprint as pp
import json

BASE_URL = "https://www.google.com/travel/hotels?utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESBgoCCAMQARogCgIaABIaEhQKBwjmDxACGAQSBwjmDxACGAUYATICEAAqCwoHKAE6A1hPRhoA&ved=0CAAQ5JsGahcKEwi4v6Ocj8D1AhUAAAAAHQAAAAAQAg&rp=OAE"
listePrices = []


with open("urls_google_hotel_link.txt", "r", encoding='utf-8') as urls, open("hotelName.txt", "r") as names, open("hotel_prices.json", "w+", encoding='utf-8') as output:
  try:
    for (url, name) in zip(urls, names):
      row = url.strip('\n')
      browser = webdriver.Firefox()
      browser.get(row)
      print(browser.title)
      res2 = browser.page_source
      
      time.sleep(1)
      soup = BeautifulSoup(res2, "html.parser")
      
      listItem = soup.select('.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a')
      listItem = listItem[2:]
      obj = dict()
      obj['name'] = name.strip('\n')
      listInfo = []
      for item in listItem:
        infoDict = {}
        infoDict['link'] = item['href']
        logo = item.select_one('.Ab0FDe.XK9Blb')
        infoDict['logo'] = logo.get('src') if logo.get('src') else logo.get('data-src')
        infoDict['website'] = item.select_one('.FjC1We.ogfYpf.zUyrwb').text
        infoDict['price'] = item.select_one('.pNExyb > .MW1oTb').text if item.select_one('.pNExyb > .MW1oTb') else item.select_one('.qeZJob > .MW1oTb').text
        infosBasic = item.select('.r1Jjcc.x4RNH span')
        infoDict['infos'] = [elt.text for elt in infosBasic]
        listInfo.append(infoDict)
        
      obj['options'] = listInfo
      listePrices.append(obj)
        
      
      """ pp.pprint(soup.prettify()) """
      browser.quit()
      """ break """
  except Exception:
    print(traceback.format_exc())
    
  json.dump(listePrices, output, indent=2, ensure_ascii=False)
    
    
    
""" .R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a  -->  link

.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a .Ab0FDe.XK9Blb  -->  logo

.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a .FjC1We.ogfYpf.zUyrwb  -->  name

.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a .r1Jjcc.x4RNH span  -->  infos

.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a .pNExyb > .MW1oTb  --> price """