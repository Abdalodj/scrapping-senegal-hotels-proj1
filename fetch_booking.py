import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import traceback
import pprint as pp
import json

listeLink = []
liste = []

with open("test.html", 'r+', encoding='utf-8') as test, open("sup.json", "w+", encoding='utf-8') as output:
  count = 1
  info = {
      "name": "",
      "mediaUrls": [],
      "hotelServices": []
    }
  row = "https://www.booking.com/hotel/sn/dakar.fr.html?selected_currency=XOF&changed_currency=1&top_currency=1&lang=fr&group_adults=2&no_rooms=1"
  """ test.truncate(0) """
  row = row.strip('\n')
  try:
    res1 = req.get(row.strip('\n'))
    print('res1')
    print(res1)
    if res1.ok:
        print('Page ' + str(count))
        print('Fetch info')
        soup = BeautifulSoup(res1.text, "html.parser")
        services = soup.select('.bui-grid__column > .clearfix > .important_facility')
        title = soup.select_one('#hp_hotel_name').text.strip('\n')
        info['hotelServices'] = [srv.text.strip('\n') for srv in services]
        info['name'] = title.replace('\n', ' ')

    time.sleep(3)
    print('Fetch img for ' + info['name'])
    browser = webdriver.Firefox()
    browser.get(row)
    elt = browser.find_element(By.CSS_SELECTOR, '.bh-photo-grid-thumb-more-inner-2')
    elt.click()
    res2 = browser.page_source
    time.sleep(1)
    soup = BeautifulSoup(res2, "html.parser")
    """ prettyHTML = soup.prettify()
    test.write(str(prettyHTML))
    time.sleep(1)
    webpage = test.read()
    soup = BeautifulSoup(webpage, "html.parser") """
    imgBlocks = soup.select('.bh-photo-modal-masonry-grid-item > a > img')
    print("N. d'image : " + str(len(imgBlocks)))
    info['mediaUrls'] = [img.get('src') if img.get('src') else img.get('data-src') for img in imgBlocks]

    print('Adding !!!')
    liste.append(info)

  except Exception:
    print(traceback.format_exc())

  count += 1
  """ if count == 3: break """
  time.sleep(3)

  json.dump(liste, output, indent=2, ensure_ascii=False)


print(len(liste))