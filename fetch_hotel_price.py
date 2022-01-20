from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import traceback
import pprint as pp
import json

BASE_URL = "https://www.google.com/travel/hotels?utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESBgoCCAMQARogCgIaABIaEhQKBwjmDxACGAQSBwjmDxACGAUYATICEAAqCwoHKAE6A1hPRhoA&ved=0CAAQ5JsGahcKEwi4v6Ocj8D1AhUAAAAAHQAAAAAQAg&rp=OAE"
listeHotelName = []

with open("hotelName.txt", "r", encoding='utf-8') as names, open("sup2.json", "w+", encoding='utf-8') as output:
  try:
    for row in names:
      row.strip('\n')
      browser = webdriver.Firefox()
      browser.get(BASE_URL)
      inputs = browser.find_elements(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')
      inputElement = inputs[1]
      inputElement.clear()
      time.sleep(1)
      inputElement.click()
      time.sleep(1)
      inputElement.send_keys(str(row))
      time.sleep(1)
      inputElement.send_keys(Keys.ENTER)
      time.sleep(5)
      buts = browser.find_elements(By.CSS_SELECTOR, '.cA1bge.RCpQOe')
      button = buts[0]
      button.click()
      res2 = browser.page_source
      """ time.sleep(1)
      soup = BeautifulSoup(res2, "html.parser")
      pp.pprint(soup.prettify()) """
      time.sleep(3)
      #browser.close()
      break
  except Exception:
    print(traceback.format_exc())