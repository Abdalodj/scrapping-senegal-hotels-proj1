import requests
from bs4 import BeautifulSoup
import time

""" links = [] 

for i in range(26):
  url = 'http://example.python-scraping.com/places/default/index/' + str(i)
  response = requests.get(url)

  if response.ok:
    print('Page '+ str(i))
    soup = BeautifulSoup(response.text, "html.parser")
    contents = soup.findAll('td')
    links +=  ['http://example.python-scraping.com' + td.find('a')['href'] for td in contents]
    time.sleep(3)
  else:
    print('err')

with open('urls_sample.txt', 'w+') as file:
  for link in links:
    file.write(link + '\n')
  
  file.close """

""" with open('urls_sample.txt', 'r') as file:
  for row in file:
    print(row) """

url = 'http://example.python-scraping.com/places/default/view/Afghanistan-1'