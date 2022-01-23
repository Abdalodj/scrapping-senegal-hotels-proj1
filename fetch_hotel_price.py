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


with open("hotelName.txt", "r", encoding='utf-8') as names, open("urls_google_hotel_link.txt", "w+") as output: 
  try:
    for row in names:
      row.strip('\n')
      browser = webdriver.Firefox()
      browser.get(BASE_URL)
      # Save the window opener (current window, do not mistaken with tab... not the same)
      inputs = browser.find_elements(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')
      print(browser.title)
      inputElement = inputs[1]
      inputElement.clear()
      time.sleep(1)
      inputElement.click()
      time.sleep(1)
      inputElement.send_keys(str(row))
      time.sleep(1)
      inputElement.send_keys(Keys.ENTER)
      time.sleep(5)
      browser.implicitly_wait(10)
      button = browser.find_element(By.CSS_SELECTOR, 'a.aS3xV.lRagtb.US5C9c')
      browser.page_source
      print(browser.title)
      button.click()
      browser.switch_to.window(browser.window_handles[-1])
      time.sleep(5)
      print(browser.title)
        
      print('testa')
      
      """ time.sleep(20) """
      print(browser.title)
      url = browser.current_url
      print(url)
      output.write(url + '\n')
      
      """ res2 = browser.page_source
      
      time.sleep(1)
      soup = BeautifulSoup(res2, "html.parser")
      
      listItem = soup.select('.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a')
      obj = dict()
      obj['name'] = row
      listInfo = []
      for item in listItem:
        infoDict = {}
        infoDict['link'] = item['href']
        logo = item.select_one('.Ab0FDe.XK9Blb')
        infoDict['logo'] = logo.get('src') if logo.get('src') else logo.get('data-src')
        infoDict['website'] = item.select_one('.FjC1We.ogfYpf.zUyrwb').text
        infosBasic = item.select('.pNExyb > .MW1oTb')
        infoDict['infos'] = [elt.text for elt in infosBasic]
        listInfo.append(infoDict)
        
      obj['prices'] = listInfo
      listePrices.append(obj)
        
      json.dump(listePrices, output, indent=2, ensure_ascii=False)   """
        
      
      """ pp.pprint(soup.prettify()) """
      browser.quit()
      time.sleep(10)
  except Exception:
    print(traceback.format_exc())
    
    
    
""" , open("sup2.json", "w+", encoding='utf-8') as output """
""" .R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a  -->  link

.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a .Ab0FDe.XK9Blb  -->  logo

.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a .FjC1We.ogfYpf.zUyrwb  -->  name

.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a .r1Jjcc.x4RNH span  -->  infos

.R09YGb.WCYWbc > .vxYgIc > span > .KQO6ob a .pNExyb > .MW1oTb  --> price """